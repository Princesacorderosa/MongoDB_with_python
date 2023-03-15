#in this example we'll work with database "bank" contains "accounts" collection
#if we want to find the document that matches id: "_id": ObjectId("62d6e04ecab6d8e1304974ae")

import pprint
import os

from dotenv import load_dotenv
from pymongo import MongoClient

#import ObjectId from bson package to enable querying by ObjectId
from bson.objectid import ObjectId
#more details here: https://api.mongodb.com/python/3.3.1/tutorial.html#querying-by-objectid

#Load config from .env file
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

#Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

#filter in form of dictionary that specifies the query
# Query by ObjectId
document_to_find = {"_id": ObjectId("62d6e04ecab6d8e1304974ae")}

# Write an expression that retrieves the document matching the query constraint in the 'accounts' collection.
result = accounts_collection.find_one(document_to_find)
pprint.pprint(result)

client.close()