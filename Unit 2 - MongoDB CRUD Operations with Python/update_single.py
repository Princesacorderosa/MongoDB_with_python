#the update_one() method has two required parameters: a filter document that matches the document to update, and an update document that specifies the modifications to apply. 
#its syntax is: db.collection.update_one(<filter>, <update>)
#In this example, the filter is assigned to the document_to_update variable, and the update is assigned to the add_to_balance variable.

#update_one() returns a result. In this example, we use the result to print a confirmation of the number of documents that were updated.
#We also print the target document before and after the update. This way, we can confirm that the specified modification has been applied.

import pprint
import os

from dotenv import load_dotenv
from pymongo import MongoClient

#Load config from .env file
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

#Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts

# Filter
document_to_update = {"_id": ObjectId("62d6e04ecab6d8e130497482")}

# Update
add_to_balance = {"$inc": {"balance": 100}}

# Print original document
pprint.pprint(accounts_collection.find_one(document_to_update))

# Write an expression that adds to the target account balance by the specified amount.
result = accounts_collection.update_one(document_to_update, add_to_balance)
#it returns the number of documents that were modified , which is 0 or 1
print("Documents updated: " + str(result.modified_count))

# Print updated document
pprint.pprint(accounts_collection.find_one(document_to_update))

client.close()