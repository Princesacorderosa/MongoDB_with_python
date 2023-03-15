
#if the inserted file does not have "_id" field, MongoDB will generate one automatically
#if we insert the document into a collection and the retrieve it from the database, will include "_id"
# the value of _id field is an instance of the ObjectID type

#to work with BSON ObjectId data type, use `bson` package in pymongo:
#bson.objectid.ObjectId
new_document = {
    "_id": ObjectId('634705cb23f1f0779c7a7525'),
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
