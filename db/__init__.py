from dotenv import load_dotenv, find_dotenv
import os
from pymongo import MongoClient

load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

connection_string = f"mongodb+srv://luizfilho:{password}@cluster0.uzqxw0y.mongodb.net/?retryWrites=true&w=majority"

client = MongoClient(connection_string)