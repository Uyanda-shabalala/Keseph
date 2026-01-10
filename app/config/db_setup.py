
import mysql.connector

db=mysql.connector.connect(
        user= "root",
        host= "localhost",
        password= ""
    )

cur=db.cursor()
cur.execute("CREATE DATABASE IF NOT EXISTS Keseph_DB")

cur.execute("USE Keseph_DB")
cur.execute("CREATE TABLE IF NOT EXISTS Users (id INT AUTO_INCREMENT PRIMARY KEY, firstname VARCHAR(255), surname VARCHAR(255), email VARCHAR(255), password VARCHAR(255), cell VARCHAR(20))")
    

db.commit()
cur.close()
db.close()