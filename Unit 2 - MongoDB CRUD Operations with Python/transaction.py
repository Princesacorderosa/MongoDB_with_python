#must have an active database connection to create a transaction!!

#1. To define the callback: In the callback, include the required parameter, which is the client session. 
#In the following example, there are four keyword parameters specific to this bank transfer: transfer_id, account_id_receiver, account_id_sender, and transfer_amount.
#Within the callback function, get references to the collections that the operations will take place on.
#Write the transaction operations. Note that you must pass the session to each operation.

#2. Start a client session by calling the start_session method on the client object in a with statement.

#3. Carry out the transaction by calling with_transaction on the session object. with_transaction starts a transaction, runs the callback, and commits (or cancels if there's an error).
#'with_transaction' has one required parameter, which is the callback function that specifies the sequence of operations to perform inside the transaction. 
#In the following example, we passed in the callback_wrapper function to pass the additional arguments to the callback: transfer_id, account_id_receiver, account_id_sender, and transfer_amount.

#Note that the general best practice for passing arbitrary arguments to the callback is to use a lambda function. In this example, we used the callback wrapper for simplicity.


import os

from dotenv import load_dotenv
from pymongo import MongoClient

#Load config from .env file
load_dotenv()
MONGODB_URI = os.environ["MONGODB_URI"]

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Step 1: Define the callback that specifies the sequence of operations to perform inside the transactions.
def callback(
    session,
    transfer_id=None,
    account_id_receiver=None,
    account_id_sender=None,
    transfer_amount=None,
):

    # Get reference to 'accounts' collection
    accounts_collection = session.client.bank.accounts

    # Get reference to 'transfers' collection
    transfers_collection = session.client.bank.transfers

    transfer = {
        "transfer_id": transfer_id,
        "to_account": account_id_receiver,
        "from_account": account_id_sender,
        "amount": {"$numberDecimal": transfer_amount},
    }

    # Transaction operations
    # Important: You must pass the session to each operation

    # Update sender account: subtract transfer amount from balance and add transfer ID
    accounts_collection.update_one(
        {"account_id": account_id_sender},
        {
            "$inc": {"balance": -transfer_amount},
            "$push": {"transfers_complete": transfer_id},
        },
        session=session,
    )

    # Update receiver account: add transfer amount to balance and add transfer ID
    accounts_collection.update_one(
        {"account_id": account_id_receiver},
        {
            "$inc": {"balance": transfer_amount},
            "$push": {"transfers_complete": transfer_id},
        },
        session=session,
    )

    # Add new transfer to 'transfers' collection
    transfers_collection.insert_one(transfer, session=session)

    print("Transaction successful")

    return


def callback_wrapper(s):
    callback(
        s,
        transfer_id="TR218721873",
        account_id_receiver="MDB343652528",
        account_id_sender="MDB574189300",
        transfer_amount=100,
    )


# Step 2: Start a client session
with client.start_session() as session:
    # Step 3: Use with_transaction to start a transaction, execute the callback, and commit (or cancel on error)
    session.with_transaction(callback_wrapper)


client.close()
