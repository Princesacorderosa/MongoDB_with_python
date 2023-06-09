
#how documents are represented in Python
#the account data is structured as a python dictionary

#to be able to insert this document into a collection, we need to assign it to a variable
#will use new_document variable
new_document = {
    "account_holder": "Addison Shelton",
    "account_id": "MDB955769550",
    "account_type": "checking",
    "years_active": 5,
    "address": {
        "city": "Ridgwood",
        "zip": "11385",
        "street": "Menahan St",
        "number": "1712",
    },
    "transfers_complete": [
        "TR628105502",
        "TR197586149",
        "TR586833243",
    ],
}