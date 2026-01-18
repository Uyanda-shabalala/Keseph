from ..config.models import User
from app.config.database import get_connection
from app.config.constants import  user_exists
from flask import Flask
from flask_bcrypt import Bcrypt


def login(email,password):  
    db=get_connection()
    cur=db.cursor()

    sql= "SELECT email,password FROM Users WHERE email=%s"
    values(email,)
    cur.execute(sql,values)
    emailResult= cur.fetchone
    result=cur.fetchall()

    if emailResult:

        Bcrypt.check_password_hash()
        sql="SELECT * FROM Users WHERE email=%s AND password=%s"


        values=(email,password)
        cur.execute(sql, values)

        result=cur.fetchone()# i need to use bcrypt here to check if the hashed password matches the one enterd by the user 


    cur.close()
    db.close()

    if result:
        return {"status": "success", "message": "Login successful."}
    else:
        return {"status": "error", "message": "Invalid email or password."}
    

def create_account(firstname,surname,email,password,cell):

    newUser= User(firstname,surname,email,password,cell)

    if user_exists(newUser.email):
        return {"status": "error", "message": "User with this email already exists."}

    if not newUser.is_valid_email():
        return {"status": "error", "message": "Invalid email format."}


    db=get_connection()

    # hash the password by the user first for security reasons never trust the user to enter clean text

    hashed_password=Bcrypt.generate_password_hash(password) # use flask's  flask-bcrypt bcrypt wrapper to simply hashin process by removing the whole process of adding salt and encoding......etc

    cur=db.cursor()
    sql="INSERT INTO Users (firstname,surname,email,password,cell) VALUES (%s,%s,%s,%s,%s)"
    values=(newUser.fullName,newUser.surname,newUser.email,hashed_password,newUser.phone)
    cur.execute(sql, values)

    cur.close()
    db.commit()
    db.close()

    return {"status": "success", "message": "Account created successfully."}# return status has chnaged so that the reponse can be used in the front end by js 


    


    