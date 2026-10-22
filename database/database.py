from peewee import SqliteDatabase, CharField, ForeignKeyField, Model, TextField
from flask_login import UserMixin

db = SqliteDatabase("database.db")

class Usuario(Model, UserMixin):
    username = CharField(unique=True)
    senha = CharField()
    salt = CharField()
    
    class Meta:
        database = db
    
class Nota(Model):
    username = ForeignKeyField(Usuario, backref="notas")
    texto = TextField()
    
    class Meta:
        database = db