import scrapy
import json
import os
from scrapy.exceptions import CloseSpider

class QuotesSpider(scrapy.Spider):
    authors_filename = 'authors.json'
    quotes_filename = 'quotes.json'

    allowed_domains = ['quotes.toscrape.com']
    start_urls = ['http://quotes.toscrape.com']


    name = "quotes"
    custom_settings = {
        "TWISTED_REACTOR": "twisted.internet.asyncioreactor.AsyncioSelectorReactor"
    }
    authors = []
    quotes = []

    # def start_requests(self):
    #     # Define the URL pattern to scrape
    #     base_url = "http://quotes.toscrape.com/page/{}/"
    #     page_number = 1

    #     # Start scraping from the first page and keep going until no quotes are found
    #     while True:
    #         url = base_url.format(page_number)
    #         yield scrapy.Request(url=url, callback=self.parse)
    #         page_number += 1

    def parse(self, response):
        # Check if there are quotes on the page
        quotes = response.css(".quote")
        if quotes:
            for quote in quotes:
                # Extract data for each quote
                text = quote.css(".text::text").get()
                author = quote.css(".author::text").get()
                tags = quote.css(".tags .tag::text").getall()

                # Store quote data in quotes.json
                self.quotes.append({
                    "quote": text,
                    "author": author,
                    "tags": tags
                })
                

                # Extract author information and store in authors.json
                author_url = quote.css(".author + a::attr(href)").get()
                if author_url:
                    author_page = response.urljoin(author_url)
                    yield scrapy.Request(author_page, callback=self.parse_author)
                
                next_link = response.xpath("//li[@class='next']/a/@href").get()
                if next_link:
                    yield scrapy.Request(url=self.start_urls[0] + next_link)
        # else:
        #     raise CloseSpider("No quotes found on this page.")

    def parse_author(self, response):
        # Extract author information
        fullname = response.css(".author-title::text").get()
        born_date = response.css(".author-born-date::text").get()
        born_location = response.css(".author-born-location::text").get()
        description = response.css(".author-description::text").get()

        # Store author data in authors list
        self.authors.append({
            "fullname": fullname.strip(),
            "born_date": born_date.strip(),
            "born_location": born_location.strip(),
            "description": description.strip()
        })

    def closed(self, reason):
        current_dir = os.path.dirname(os.path.abspath(__file__))

        # Navigate up multiple levels to reach the project_directory
        project_dir = os.path.dirname(os.path.dirname(os.path.dirname(current_dir)))

        # Define the path to the json folder relative to the project_directory
        json_folder = os.path.join(project_dir, 'json')

        # Create the json folder if it doesn't exist
        os.makedirs(json_folder, exist_ok=True)

        # Construct the full path to the JSON files
        authors_path = os.path.join(json_folder, self.authors_filename)
        quotes_path = os.path.join(json_folder, self.quotes_filename)

        # Dump authors and quotes data to JSON files after spider is closed
        with open(authors_path, "w") as authors_file:
            json.dump(self.authors, authors_file, indent=2)
            print(f'============JSON file created at: {self.authors_filename}')
        with open(quotes_path, "w") as quotes_file:
            json.dump(self.quotes, quotes_file, indent=2)
            print(f'============JSON file created at: {self.quotes_filename}')