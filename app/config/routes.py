from flask import Flask, request, jsonify


from ..logic.User_Logic import login,create_account

# apis always return json responses 
app = Flask(__name__)

@app.route("/api/login", methods=["POST"])
def login_route():
    data= request.get_json() 

    if data is None:
        return jsonify({"error": "Invalid JSON or missing Content-Type: application/json"}), 400
    
    email=data.get('email')
    pw=data.get('password')
    result=login(email,pw)
    return(jsonify(result))


@app.route("/api/createaccount",methods=["POST"])

def create_account_route():
    data=request.get_json()
    

    if data is None: 
        return jsonify({"error": "Invalid JSON or missing Content-Type: application/json"}), 400
    

    name=data.get('firstname')
    surname=data.get('surname')
    email=data.get('email')
    pw=data.get('password')
    cell=data.get('phone')


    
    result=create_account(name,surname,email,pw,cell)
    return(jsonify(result))


@app.route("/api/addexpense", methods=["POST"])
def add_expense_route():
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Invalid JSON or missing Content-Type: application/json"}), 400

    amount = data.get('amount')
    method = data.get('method')
    category = data.get('category')
    description = data.get('description')


@app.route("/api/addincome", method=["POST"])

def add_income_route(): 
        
    data = request.get_json()

    if data is None:
        return jsonify({"error": "Invalid JSON or missing Content-Type: application/json"}), 400
