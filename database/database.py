from peewee import SqliteDatabase, CharField, ForeignKeyField, Model, TextField, DateTimeField
import datetime
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
    criado_em = DateTimeField(default=datetime.datetime.now)
    titulo = CharField()
    texto = TextField()
    
    class Meta:
        database = db