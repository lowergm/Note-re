from flask import Blueprint, render_template, request

pages = Blueprint("pages", __name__)

@pages.route("/")
def home():
    return render_template("index.html")

@pages.route("/login")
def login():
    return render_template("login.html")

@pages.route("/cadastrar")
def cadastrar():
    return render_template("cadastro.html")