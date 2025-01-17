
from flask import Flask,redirect,url_for,make_response
from flask import render_template
from flask import request,session,jsonify
import os
import pathlib
import json

# creates a Flask application, named app
app = Flask(__name__,static_folder='templates/static')

@app.route("/",methods=["GET","POST"])
def login():   
    if(request.method=="GET"):
        return render_template("index.html");
    else:
        usuario=request.form["usuario"];
        session["usuario"]=usuario;
        return redirect(url_for("chat"));

@app.route("/chat")
def chat():
    if("usuario" in session.keys()):
        return render_template("chat.html",usr=session["usuario"]);
    else:
        return redirect(url_for("login"));

@app.route("/apimsg",methods=["POST"])
def api():
    mensaje=request.get_json()
    print(session["usuario"],mensaje["mensaje"]);
    return session["usuario"] +": " +mensaje["mensaje"];

# run the application
if __name__ == "__main__":
    app.secret_key = "generador de claves de sesión"
    app.run(host="localhost",port=8085,debug=True)