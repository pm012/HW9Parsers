from models import Author, Quote
from connect import get_mongo_connection


# Search quotes by tag or author name
def search_quotes(command):
    if command.startswith("name:"):
        author_name = command.split(":")[1].strip()
        author = Author.objects(fullname=author_name).first()
        if author:
            quotes = Quote.objects(author=author)
            return [quote.to_json().encode("utf-8") for quote in quotes]
        else:
            return []

    elif command.startswith("tag:"):
        tags = command.split(":")[1].strip().split(",")
        quotes = Quote.objects(tags__in=tags)
        return [quote.to_json().encode("utf-8") for quote in quotes]

    elif command.startswith("tags:"):
        tags = command.split(":")[1].strip().split(",")
        quotes = Quote.objects(tags__all=tags)
        return [quote.to_json().encode("utf-8") for quote in quotes]

    elif command == "exit":
        return "Exiting...".encode("utf-8")

    else:
        return "Invalid command!".encode("utf-8")
    
if __name__ == "__main__":
    # Search quotes in an endless loop
    with get_mongo_connection():
        while True:
            command = input("Enter command (name:, tag:, exit): ")
            result = search_quotes(command)
            if command == "exit":
                print(result)
                break;
            if result:
                for item in result:
                    print(item.decode("utf-8"))
            else:
                print("No quotes found.")