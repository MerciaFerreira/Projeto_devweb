from app import db


class Livro(db.Model):

    __tablename__ = 'livro'

   
    def __init__(self, id, titulo, autor, editora):

        self.id = id
        self.titulo = titulo
        self.autor = autor
        self.editora = editora