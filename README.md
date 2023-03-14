## Using MongoDB with Python course

This repository contains my exercises for the MongoDB University course "Using MongoDB with Python". 
The course explains how to utilize MongoDB as a backing database for Python applications.  
MongoDB driver documentation website: https://www.mongodb.com/docs/drivers/

The course is divided into three units:

### Unit 1: Connecting to MongoDB in Python 
How to connect a Python application to a MongoDB Atlas cluster by using 'pymongo' driver. 

* Lesson 1: Using MongoDB Python Client Libraries  
There are two Python drivers:  
**PyMongo** for synchronous applications and **Motor** for asynchronous applications. 

* Lesson 2: Connecting to an Atlas Cluster in Python Applications  
To install PyMongo 1st need to create a **directory** for the project and 2nd create and activate a **python virtual environment**   
To install the driver and also DNS python, in project directory write: <pre> python3 -m pip install 'pymongo[srv]' </pre>
And inside the directory created, run the [connection.py](https://github.com/Princesacorderosa/MongoDB_with_python/blob/main/Unit%201%20-%20Connecting%20to%20MongoDB%20in%20Python/connection.py) file (inside Unit 1 folder) 

* Lesson 3: Troubleshooting a MongoDB Connection in Python Applications
Ater set up and activate virtual environment ".env", run the rest of the code [connection2.py](https://github.com/Princesacorderosa/MongoDB_with_python/blob/main/Unit%201%20-%20Connecting%20to%20MongoDB%20in%20Python/connection2.py)  
If the error message is:  
 **"ServerSelectionTimeoutError"**, then should be a problem IP address without access. (solution: add IP adress to network access);  
 **"OperationFailure" "Authentication failed"**, check if <username> or <password> were updated in the connection string.
 
 
### Unit 2: MongoDB CRUD Operations with Python  
learn about the four basic CRUD operations in MongoDB: Create, Read, Update, and Delete. You will also learn how to perform these operations using the pymongo driver in your Python applications.

Unit 3: Aggregation with Python

