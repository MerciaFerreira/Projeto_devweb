import uuid
import datetime
from app import db 
from app.Entidades import Reserva

def save_reserva(dados):
    pass

def get_all_reserva():
    pass

def get_reserva(id):
    pass

def update_reserva(id):
    pass

def delete_reserva(id):
    pass

def save(dados):
    db.session.add(dados)
    db.session.commit()

