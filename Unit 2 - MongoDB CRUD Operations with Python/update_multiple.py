#The update_many() method also has two required parameters: a filter document that matches the document to update, and an update document that specifies the modifications to apply. 
#In this example, the filter is assigned to the select_accounts variable, and the update is assigned to the set_field variable. Note that in this update, we define a new field and set its initial value.
#update_many() returns a result. In this example, we use the result to print out a confirmation of the number of documents that matched and were modified by the operation. #We also print out one sample document after the update. This way, we can confirm that the specified modification has been applied. 


import pprint
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

# Get reference to 'accounts' collection
accounts_collection = db.accounts

# Filter
select_accounts = {"account_type": "savings"}

# Update
set_field = {"$set": {"minimum_balance": 100}}

# Write an expression that adds a 'minimum_balance' field to each savings acccount and sets its value to 100.
result = accounts_collection.update_many(select_accounts, set_field)

print("Documents matched: " + str(result.matched_count))
print("Documents updated: " + str(result.modified_count))
pprint.pprint(accounts_collection.find_one(select_accounts))

client.close()