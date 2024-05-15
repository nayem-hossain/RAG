import time
from selenium import webdriver
from parsel import Selector
import os

def scrape_api_documentation(url, output_file):
    # Set up Selenium WebDriver
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=options)

    # Navigate to the website
    driver.get(url)

    # Wait for the page to load
    time.sleep(5)  # Adjust the sleep time as needed

    # Get the page source
    html = driver.page_source

    # Parse the HTML using Parsel
    selector = Selector(text=html)

    # Extract response types
    response_types = []
    response_sections = selector.css('div[data-section-id^="operation/"]')
    for section in response_sections:
        section_data = {}
        
        # Extract endpoint data
        endpoint_element = section.css('div.sc-jSFjdj.sc-gKAaRy.dYGhuI.fTsuzH > div.sc-EZqKI.iONckA > button')
        endpoint_data = endpoint_element.css('span::text').getall()
        section_data['Endpoint'] = '/'.join(endpoint_data)
        
        section_title = section.css('h2::text').get()
        section_data['HTTP Method'] = section_title

        method_description = section.css('div.sc-hKFxyN.hutltu > div.sc-iGkqmO.jEmHgI > div > p::text').get()
        section_data['Method Description'] = method_description if method_description else ''

        parameters_table = section.css('div.sc-hKFxyN.hutltu > div.sc-iGkqmO.jEmHgI > div > table')
        if parameters_table:
            parameters_data = []
            parameter_rows = parameters_table.css('tr')
            for row in parameter_rows[1:]:  # Skip header row
                parameter_name = row.css('td:nth-child(1)::text').get()
                parameter_type = row.css('td:nth-child(2)::text').get()
                parameter_value_type = row.css('td:nth-child(3)::text').get()
                parameter_description = row.css('td:nth-child(4)::text').get()
                parameters_data.append({
                    'Name': parameter_name,
                    'Key Type': parameter_type,
                    'Value Type': parameter_value_type,
                    'Description': parameter_description
                })
            section_data['Parameters'] = parameters_data
        else:
            section_data['Parameters'] = []

        response_data = []
        if parameters_table:
            responses = section.css('div.sc-hKFxyN.hutltu > div:nth-child(7) > div > button')
        else:
            responses = section.css('div.sc-hKFxyN.hutltu > div:nth-child(4) > div > button')

        for response_element in responses:
            response_code = response_element.css('strong::text').get()
            response_description = response_element.css('p::text').get()
            if response_code and response_description:
                response_data.append({
                    'Code': response_code,
                    'Description': response_description
                })
        section_data['Responses'] = response_data
        response_types.append(section_data)

    # Write the scraped data to a text file
    with open(output_file, 'w', encoding='utf-8') as f:
        for section_data in response_types:
            f.write(f"Endpoint: {section_data['Endpoint']}\n")  # Write the endpoint data
            f.write(f"HTTP Method: {section_data['HTTP Method']}\n")
            f.write(f"Method Description: {section_data['Method Description']}\n")
            if section_data['Parameters']:
                f.write("Parameters:\n")
                for parameter in section_data['Parameters']:
                    f.write(f" Name: {parameter['Name']}, Key Type: {parameter['Key Type']}, Value Type: {parameter['Value Type']}, Description: {parameter['Description']}\n")
            f.write("Responses:\n")
            for response in section_data['Responses']:
                f.write(f" Code: {response['Code']}, Description: {response['Description']}\n")
            f.write('\n')
    print(f"Scraped data saved to {output_file}")

    # Close the browser
    driver.quit()
    

def write_scraped_data(response_types, output_folder):
    # Creating the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    all_data = []  # To store all scraped data for consolidation

    for index, section_data in enumerate(response_types):
        filename = os.path.join(output_folder, f"scraped_data_{index + 1}.txt")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"Endpoint: {section_data['Endpoint']}\n")  # Write the endpoint data
            f.write(f"HTTP Method: {section_data['HTTP Method']}\n")
            f.write(f"Method Description: {section_data['Method Description']}\n")
            if section_data['Parameters']:
                f.write("Parameters:\n")
                for parameter in section_data['Parameters']:
                    f.write(f" Name: {parameter['Name']}, Key Type: {parameter['Key Type']}, Value Type: {parameter['Value Type']}, Description: {parameter['Description']}\n")
            f.write("Responses:\n")
            for response in section_data['Responses']:
                f.write(f" Code: {response['Code']}, Description: {response['Description']}\n")
            f.write('\n')
        print(f"Scraped data saved to {filename}")

        # Append data to all_data for consolidation
        with open(filename, 'r', encoding='utf-8') as f:
            all_data.append(f.read() + '\n\n')

    # Consolidate all data into a single text file
    all_data_filename = os.path.join(output_folder, "all_scraped_data.txt")
    with open(all_data_filename, 'w', encoding='utf-8') as f:
        f.write(''.join(all_data))
    print(f"All scraped data saved to {all_data_filename}")


if __name__ == "__main__":
    url = 'https://api.recommender.gigalogy.com/v1/documentation'
    output_file = 'scraped_data.txt'
    scrape_api_documentation(url, output_file)
