from data_loader_v1 import scrape_websites
from data_loader_v2 import scrape_api_documentation

def main():
        
    websites = ["https://gigalogy.com", "https://tutorial.gigalogy.com"]  # Inputted websites
    output_folder = "scraped_data"  # Folder to save the scraped data
    scrape_websites(websites, output_folder)

    # Call the scrap_api_documentation function
    url = 'https://api.recommender.gigalogy.com/v1/documentation'
    output_file = 'scraped_data.txt'
    scrape_api_documentation(url, output_file)

if __name__ == "__main__":
    main()