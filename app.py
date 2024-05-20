from flask import Flask
app=Flask(__name__)

@app.route("/")
def welcome():
    return "Hello world"

@app.route("/home")
def home():
    return "This is home"
@app.route("/hi")
def hi():
    return "hi"
# import controller.user_controllers as user_controllers
# import controller.product_controller as product_controller
from controller import *
