from flask import Flask, render_template, request, redirect, session
import sqlite3 as sql

 ## Create App ##
app = Flask(__name__)
app.secret_key = "secret123"

## Create app Routes 
@app.route("/")
@app.route("/Home")
def Home():
    return render_template("Home.html")

@app.route("/Login")
def Login():
    return render_template("Login.html")

@app.route("/Create_Account")
def Create_Account():
    return render_template("Create_Account.html")

@app.route("/Fitness_Center")
def Fitness_Center():
    return render_template("Fitness_Center.html")

@app.route("/Membership")
def Membership():
    return render_template("Membership.html")

@app.route("/Room_Hire")
def Room_Hire():
    return render_template("Room_Hire.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # Must have host='0.0.0.0'
