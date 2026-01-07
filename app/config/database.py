#this will be for the database connection 
import mysql.connector


db=mysql.connector.connect(
    user= "admin",
    host= "localhost",
    password= "admin"
)

cur=db.cursor()



