#this will be for all the classes 
 
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
    

    def validate_email(self):

      try :
          emailinfo=validate_email(self.email,EmailNotValidError)
      except EmailNotValidError as e: 
           print(e)     