#this will be for the database connection 
import mysql.connector

def get_connection():
    db=mysql.connector.connect(
        user= "root",
        host= "localhost",  
        password= "",
        database= "Keseph_DB"
    )   
    return db



  

 


