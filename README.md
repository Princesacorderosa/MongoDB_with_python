# Using MongoDB with Python course

This repository contains my exercises for the MongoDB University course "Using MongoDB with Python". 
The course explains how to utilize MongoDB as a backing database for Python applications.  
MongoDB driver documentation website: https://www.mongodb.com/docs/drivers/

The course is divided into three units:

## Unit 1: Connecting to MongoDB in Python 
How to connect a Python application to a MongoDB Atlas cluster by using **`pymongo`** driver. 

* ### Lesson 1: Using MongoDB Python Client Libraries  
  There are two Python drivers:  
  **PyMongo** for synchronous applications and **Motor** for asynchronous applications. 

* ### Lesson 2: Connecting to an Atlas Cluster in Python Applications  
  To install PyMongo 1st need to create a **directory** for the project and 2nd create and activate a **python virtual environment**   
  To install the driver and also DNS python, in project directory write:<pre>python3 -m pip install 'pymongo[srv]'</pre>
  And inside the directory created, run the [connection.py](https://github.com/Princesacorderosa/MongoDB_with_python/blob/main/Unit%201%20-%20Connecting%20to%20MongoDB%20in%20Python/connection.py) file (inside Unit 1 folder) 

* ### Lesson 3: Troubleshooting a MongoDB Connection in Python Applications
  Ater set up and activate virtual environment ".env", run the rest of the code [connection2.py](https://github.com/Princesacorderosa/MongoDB_with_python/blob/main/Unit%201%20-%20Connecting%20to%20MongoDB%20in%20Python/connection2.py)  
  If the error message is:  
  **"ServerSelectionTimeoutError"**, then should be a problem IP address without access. (solution: add IP adress to network access);  
  **"OperationFailure" "Authentication failed"**, check if <username> or <password> were updated in the connection string.
 
 
## Unit 2: MongoDB CRUD Operations with Python  
learn about the four basic CRUD operations in MongoDB: Create, Read, Update, and Delete. You will also learn how to perform these operations using the pymongo driver in your Python applications.  
The documents used in this Unit are available in [Unit 2](https://github.com/Princesacorderosa/MongoDB_with_python/tree/main/Unit%202%20-%20MongoDB%20CRUD%20Operations%20with%20Python) file.  

* ### Lesson 1: Working with MongoDB Documents in Python  
  BSON (binary JSON) is data format that MongoDB uses to organize and store data. BSON supports more data types than JSON. PyMongo represents BSON documents as python dictionaries.  
  
  Every document requires `_id` field, acts as **primary key**. If inserted document doesn't have one, MongoDB will generate an ObjectId value for it.  
  For example: the [sample_doc.py](https://github.com/Princesacorderosa/MongoDB_with_python/blob/main/Unit%202%20-%20MongoDB%20CRUD%20Operations%20with%20Python/sample_doc.py) (on Unit 2 file), doesn't include an `_id` field, but if we insert the document into a collection and the retrieve it from the database, will include "_id", as shown in [sample_doc2.py](https://github.com/Princesacorderosa/MongoDB_with_python/blob/main/Unit%202%20-%20MongoDB%20CRUD%20Operations%20with%20Python/sample_doc2.py)  
  To work with BSON ObjectId data type in python, use **`bson`** package in PyMongo: <pre> bson.objectid.ObjectId </pre>  

* ### Lesson 2: Inserting a Document in Python Applications
  There are 2 methods to insert documents into MongoDB:  
  `insert_one()` - inserts a single document  (to see it in action: [insert_single.py](https://github.com/Princesacorderosa/MongoDB_with_python/blob/main/Unit%202%20-%20MongoDB%20CRUD%20Operations%20with%20Python/insert_single.py) )
  `insert_many()` - inserts multiple documents   (to see it in action: [insert_multiple.py](https://github.com/Princesacorderosa/MongoDB_with_python/blob/main/Unit%202%20-%20MongoDB%20CRUD%20Operations%20with%20Python/insert_multiple.py) )
  
* ### Lesson 3: Querying a MongoDB Collection in Python Applications
  there are 2 methods to query in MongoDB:  
  `find_one()` - return a single document that matches the query, or none if there are no matches. Useful when we know there's only one doc, or interested in the 1st match.  
  example: if we want to find the document that matches id: **"_id": ObjectId("62d6e04ecab6d8e1304974ae")**  [find_single.py](https://github.com/Princesacorderosa/MongoDB_with_python/blob/main/Unit%202%20-%20MongoDB%20CRUD%20Operations%20with%20Python/find_single.py)  
  `find()` - return all documents that match a query
  example: if we want to find all accounts with balance greater than $4700 [find_multiple.py](https://github.com/Princesacorderosa/MongoDB_with_python/blob/main/Unit%202%20-%20MongoDB%20CRUD%20Operations%20with%20Python/find_multiple.py)

* ### Lesson 4: Updating Documents in Python Applications
  How to perform single and multiple documents updates, using PyMongo's methods:
  `update_one()` - update a single document that matches specified criteria. its syntax is:<pre>db.collection.update_one(<filter , <update)</pre>To demonstrate update one [update_single.py](https://github.com/Princesacorderosa/MongoDB_with_python/blob/main/Unit%202%20-%20MongoDB%20CRUD%20Operations%20with%20Python/update_single.py)

   `update_many()` - update multiple documents in single operation. its syntax is:<pre>db.collection.update_many(<filter , <update)</pre> [update_multiple.py](https://github.com/Princesacorderosa/MongoDB_with_python/blob/main/Unit%202%20-%20MongoDB%20CRUD%20Operations%20with%20Python/update_multiple.py)
   
* ### Lesson 5: Deleting Documents in Python Applications
  Methods to delete documents in MongoDB can use:  
  `delete_one()` to delete a single document. its syntax is:<pre>db.collection.delete_one(<filter)</pre> it accepts the query **filter** that matches the document we want to delete.  
  An example for this method: [delete_single.py](https://github.com/Princesacorderosa/MongoDB_with_python/blob/main/Unit%202%20-%20MongoDB%20CRUD%20Operations%20with%20Python/delete_single.py)  
  
  `delete_many()` to delete multiple documents in single operation. its syntax is:<pre>db.collection.delete_many(<filter)</pre> if query filter is empty, then all documents in collection will be deleted. 
  An example for this method: [delete_multiple.py](https://github.com/Princesacorderosa/MongoDB_with_python/blob/main/Unit%202%20-%20MongoDB%20CRUD%20Operations%20with%20Python/delete_multiple.py)
