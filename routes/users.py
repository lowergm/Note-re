from flask import Blueprint, request, redirect, url_for, flash
from database.database import Usuario
from peewee import IntegrityError
from flask_login import login_user, login_required, logout_user
import hashlib
import os
from extensions import lm

users = Blueprint("users", __name__)

@lm.user_loader
def user_loader(id):
    try:
        usuario = Usuario.get_by_id(id)
        return usuario
    except Usuario.DoesNotExist:
        return None

def hash(txt, salt):
    if salt:
        hash_obj = hashlib.pbkdf2_hmac('sha256', txt.encode(), salt, 600000)
        return hash_obj.hex(), salt.hex()
    else:
        salt = os.urandom(16)
        hash_obj = hashlib.pbkdf2_hmac('sha256', txt.encode(), salt, 600000)
    return hash_obj.hex(), salt.hex()

@users.route("/criaruser", methods=["POST"])
def new_user():
    nome = request.form.get("cadastronome")
    senha = request.form.get("cadastrosenha")
    try:
        senha, salt = hash(senha, None)
        novo_usuario = Usuario.create(username=nome.lower(), senha=senha, salt=salt)
        
        login_user(novo_usuario)
    except IntegrityError:
        flash("Este nome já está sendo usado", "cadastro")
        return redirect(url_for("pages.cadastrar"))
    return redirect(url_for('pages.notas'))

@users.route("/logaruser", methods=["POST"])
def login_usuario():
    nome = request.form.get("entrarnome")
    senha = request.form.get("entrarsenha")
    
    user = Usuario.get_or_none(Usuario.username==nome.lower())
    
    if user is None:
        flash("Usuario não encontrado", "login")
        return redirect(url_for("pages.login"))
    
    senha, salt = hash(senha, bytes.fromhex(user.salt))
    
    if senha == user.senha:
        login_user(user)
        return redirect(url_for("pages.notas"))
    else:
        return redirect(url_for("pages.login"))

@users.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("pages.login"))