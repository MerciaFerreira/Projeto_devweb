from app import db 
from app.Entidades import Livros

def save_livros(dados):
    pass

def get_all_livros():
    pass

def get_livros(id):
    pass

def update_livros(id):
    pass

def delete_livros(id):
    pass

def save(dados):
    db.session.add(dados)
    db.session.commit()

