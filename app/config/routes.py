from flask import Flask, request, jsonify


from ..logic.User_Logic import login,create_account


app = flask.Flask(__name__)

@app.route("/api/login", methods=["POST"])
def login_route():
    data= request.get_json() 
    result=login()
    
    return(result)


@app.route("/api/createaccount",methods=["POST"])

def create_account_route():
    data=request.get_json()
    result=create_account()
    return(result)
