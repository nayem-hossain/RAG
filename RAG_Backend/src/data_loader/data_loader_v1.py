import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from urllib.parse import urlparse

def scrape_websites(websites, output_folder):
    # Set up Selenium WebDriver
    options = Options()
    options.headless = False  # Run Chrome in headless mode
    driver = webdriver.Chrome(options=options)

    for website in websites:
        print(f"Scraping data from {website}")
        all_urls = get_urls(driver, website)
        print("Total URLs found:", len(all_urls))
        for url in all_urls:
            print("Scraping data from:", url)
            scrape_data_and_save(driver, url, output_folder)

    # Clean up
    driver.quit()

# Function to fetch all URLs from a webpage
def get_urls(driver, base_url):
    driver.get(base_url)
    urls = set()

    # Extract URLs from anchor tags
    for link in driver.find_elements(By.TAG_NAME, 'a'):
        href = link.get_attribute('href')
        if href:
            urls.add(href)

    return urls

# Function to scrape data from a webpage and save it to a text file
def scrape_data_and_save(driver, url, output_folder):
    driver.get(url)
    try:
        # Scraping data
        title = driver.title
        content = driver.find_element(By.TAG_NAME, 'body').text
        
        # Creating the output folder if it doesn't exist
        if not os.path.exists(output_folder):
            os.makedirs(output_folder)

        # Writing data to a text file
        filename = os.path.join(output_folder, f"{urlparse(url).netloc}-{urlparse(url).path.replace('/', '_')}.txt")
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(f"URL: {url}\n\n")
            f.write(f"Title: {title}\n\n")
            f.write(f"Content:\n{content}\n")
        print(f"Scraped data saved to {filename}")
    except NoSuchElementException:
        print("Error: Element not found on page", url)

if __name__ == "__main__":
    websites = ["https://gigalogy.com", "https://tutorial.gigalogy.com"]  # Inputted websites
    output_folder = "scraped_data"  # Folder to save the scraped data
    scrape_websites(websites, output_folder)
