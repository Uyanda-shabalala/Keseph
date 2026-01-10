import re 
from app.config.database import get_connection
def is_valid_email(email):
     # Regex pattern:
    # ^[\\w\\.-]+  -> Starts with one or more word characters, periods, or hyphens (local part)
    # @             -> Followed by an '@' symbol
    # [a-zA-Z\\d-]+ -> Followed by one or more letters, digits, or hyphens (domain name)
    # \\.           -> Followed by a period
    # [a-zA-Z]{2,}$ -> Ends with 2 or more letters (top-level domain)

    pattern = r'^[\w\.-]+@[a-zA-Z\d-]+\.[a-zA-Z]{2,}$'

       # Use re.fullmatch  to ensure the whole string matches the pattern
    if re.fullmatch(pattern, email):
        return True
    else:
        return False


    
def user_exists(email):

    db=get_connection() 
    cur=db.cursor()

    sql= "SELECT email FROM Users WHERE email=%s" 
    values=(email,)
    cur.execute(sql, values) 
    result =cur.fetchone()
     
    if result:
        cur.close()
        db.close()
        
        return True
    else:
        cur.close()
        db.close()
        return False