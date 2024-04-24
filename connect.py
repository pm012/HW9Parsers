import configparser
from mongoengine import connect


config = configparser.ConfigParser()
config.read('config.ini')
mongo_user = config.get('DB', 'user')
mongo_pass = config.get('DB', 'pass')
db_name = config.get('DB', 'db_name')
domain = config.get('DB', 'domain')

def get_mongo_connection():
    connection_uri = f"mongodb+srv://{mongo_user}:{mongo_pass}@{domain}/{db_name}?retryWrites=true&w=majority&appName=Cluster0"
    return connect(host=connection_uri, ssl=True)