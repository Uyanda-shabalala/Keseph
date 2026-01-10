from ..config.models import User
from app.config.database import get_connection
from app.config.constants import  user_exists

def login(email,password):  
    db=get_connection()
    cur=db.cursor()

    sql="SELECT * FROM Users WHERE email=%s AND password=%s"
    values=(email,password)
    cur.execute(sql, values)

    result=cur.fetchone()

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

    cur=db.cursor()
    sql="INSERINTO Users (firstname,surname,email,password,cell) VALUES (%s,%s,%s,%s,%s)"
    values=(newUser.fullName,newUser.surname,newUser.email,newUser.password,newUser.phone)
    cur.execute(sql, values)

    cur.close()
    db.commit()
    db.close()

    return {"status": "success", "message": "Account created successfully."}

    


    