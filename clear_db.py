from models import Author, Quote
from connect import get_mongo_connection




if __name__ == "__main__":
    # Load JSON data into MongoDB collections
   with get_mongo_connection():
      Author.objects.delete()
      Quote.objects.delete()
           
