#this will be for all the classes 
 
from app.config.database import get_connection
from email_validator import validate_email, EmailNotValidError

class User ():

    def __init__(self,fullName,surname,email,password,phone):
            self.fullName=fullName
            self.surname=surname
            self.email=email
            self.password=password
            self.phone=phone
    def get_name(self):
          return self.FullName 
    
    def get_surname(self):
          return self.Surname
    
    def user_exits(self):
         
         db=get_connection()

         cur=db.cursor()
         sql=cur.execute("SELECT * FROM KESEPH_DB WHERE email=%s")
         value=(sql,self.email)
            


    def validate_email(self):

      try :
          emailinfo=validate_email(self.email,EmailNotValidError)
      except EmailNotValidError as e: 
           print(e)
      
  