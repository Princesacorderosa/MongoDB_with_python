#python3 -m pip install 'pymongo[srv]'

#import mongo client class from PyMongo
#mongo client is used to initiate the connection with the database
from pymongo import MongoClient

#assign a variable to the connection string  
MONGODB_URI = "mongodb+srv://<username>:<password>@cluster0.usqsf.mongodb.net/?retryWrites=true&w=majority"
#connection string can get from MongoDB Atlas database
#remember to change username and password

#create a mongo client instance, using connection string as argument
client = MongoClient(MONGODB_URI)

#with these lines, have access to Atlas cluster via the Mongo client

#-----------
#to test the connection (by looping trough the database in the cluster)

for db_name in client.list_database_names():
    print(db_name)

#if all the databases on the cluster are printed on the terminal, means connection was successful 