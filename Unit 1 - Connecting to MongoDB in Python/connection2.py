
#lesson 3 troubleshooting
#simple python app for demo issues
#-----
#after having virtual environment set up and activated
import os

from dotenv import load_dotenv
from pymongo import MongoClient

#load config from .env file
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

#Create MongoClient instance
client = MongoClient(MONGODB_URI)

#print a list of the databases on the cluster
for db_name in client.list_database_names():
  print(db_name)
  
client.close()
