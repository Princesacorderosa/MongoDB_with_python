#if we want to find all accounts with balance greater than $4700

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

# Query
#filter to select documents, using operator $gt that represents greater than
documents_to_find = {"balance": {"$gt": 4700}}

# Write an expression that selects the documents matching the query constraint in the 'accounts' collection.
cursor = accounts_collection.find(documents_to_find)

# to print the total number of documents and the documents find by its query
num_docs = 0
for document in cursor:
    num_docs += 1
    pprint.pprint(document)
    print()
print("# of documents found: " + str(num_docs))

client.close()