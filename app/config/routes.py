import flask
from logic.User_Logic import login,create_account


app = flask.Flask(__name__)

app.route("api/login", methods=["POST"])

login()


app.route("api/createaccount",methods=["POST"])

create_account()