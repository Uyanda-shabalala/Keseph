import re 
from app.config.database import get_connection



    
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