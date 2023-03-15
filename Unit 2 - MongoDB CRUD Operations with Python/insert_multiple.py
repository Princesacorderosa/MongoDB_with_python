#to insert multiple documents into a collection, append insert_naby() to the collection object. 
#In this example, we use the result to print the _id value of the inserted documents and the number of documents.

import datetime
import os

from dotenv import load_dotenv
from pymongo import MongoClient

#Load config from .env file
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

#Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

#Get reference to 'bank' database
db = client.bank

# Get a reference to 'accounts' collection
accounts_collection = db.accounts

#because insert_many() takes an iterable of documents to insert:
#we put the accounts into a list and assign it to variable called new_accounts
new_accounts = [
    {
        "account_id": "MDB011235813",
        "account_holder": "Ada Lovelace",
        "account_type": "checking",
        "balance": 60218,
    },
    {
        "account_id": "MDB829000001",
        "account_holder": "Muhammad ibn Musa al-Khwarizmi",
        "account_type": "savings",
        "balance": 267914296,
    },
]

# Write an expression that inserts the documents in 'new_accounts' into the 'accounts' collection.
result = accounts_collection.insert_many(new_accounts)

document_ids = result.inserted_ids
#print number of documents inserted
print("# of documents inserted: " + str(len(document_ids)))
print(f"_ids of inserted documents: {document_ids}")

#to close the database connection
client.close()

#running this file, the _id value that MongoDB created is printed out