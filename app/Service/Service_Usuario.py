import uuid
import datetime
from app import db 
from app.Entidades import Usuario

def save_users(dados):
    pass

def get_all_users():
    pass

def get_users(id):
    pass

def update_users(id):
    pass

def delete_users(id):
    pass

def save(dados):
    db.session.add(dados)
    db.session.commit()

