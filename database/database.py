from peewee import MySQLDatabase, CharField, ForeignKeyField, Model, TextField, DateTimeField
import datetime
from flask_login import UserMixin
from dotenv import load_dotenv
import os
import ssl

load_dotenv()
ssl_context = ssl.create_default_context()

db = MySQLDatabase(
    os.getenv("DB_NAME"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT")),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASSWORD"),
    ssl=ssl_context
)

class Usuario(Model, UserMixin):
    username = CharField(unique=True)
    senha = CharField()
    salt = CharField()
    
    class Meta:
        database = db
    
class Nota(Model):
    username = ForeignKeyField(Usuario, backref="notas")
    criado_em = DateTimeField(default=datetime.datetime.now)
    titulo = CharField()
    texto = TextField()
    
    class Meta:
        database = db