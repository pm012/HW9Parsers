from models import Author, Quote
import json
from connect import get_mongo_connection

AUTHORS_PATH = "./json/authors.json"
QUOTES_PATH = "./json/quotes.json"

# Load JSON data into MongoDB
def load_authors_from_json(filename):
    with open(filename, "r") as file:
        authors_data = json.load(file)
        with get_mongo_connection():
            for author_data in authors_data:
                Author(**author_data).save()

def load_quotes_from_json(filename):
    with open(filename, "r") as file:
        quotes_data = json.load(file)
        for quote_data in quotes_data:
            author_name = quote_data["author"]
            author = Author.objects(fullname=author_name).first()
            with get_mongo_connection():
                if author:
                    quote_data["author"] = author
                    Quote(**quote_data).save()



if __name__ == "__main__":
    # Load JSON data into MongoDB collections
    load_authors_from_json(AUTHORS_PATH)
    load_quotes_from_json(QUOTES_PATH)
