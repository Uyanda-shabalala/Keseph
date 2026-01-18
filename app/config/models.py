#this will be for all the classes 
import re 
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

    def is_valid_email(self):
     # Regex pattern:
    # ^[\\w\\.-]+  -> Starts with one or more word characters, periods, or hyphens (local part)
    # @             -> Followed by an '@' symbol
    # [a-zA-Z\\d-]+ -> Followed by one or more letters, digits, or hyphens (domain name)
    # \\.           -> Followed by a period
    # [a-zA-Z]{2,}$ -> Ends with 2 or more letters (top-level domain)

      pattern = r'^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$'

       # Use re.fullmatch  to ensure the whole string matches the pattern
      if re.fullmatch(pattern, self.email):
        return True
      else:
        return False
      

class Expense():
    
    def __init__(self,amount,description,type,id):

        self.amount=amount
        self.description=description
        self.type=type
        self.type=id    
        
    def is_Valid_amount(self):
        
        if self.amount<0 :
            return False
        return True 