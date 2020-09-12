from app import db

autores = db.Table(
    'autores',
    db.Column(
        'livro_id', db.Integer, db.ForeignKey('livro.id'), primary_key=True
    ),
    db.Column(
        'autor_id', db.Integer, db.ForeignKey('autor.id'), primary_key=True
    )
)


class Livro(db.Model):

    __tablename__ = 'livro'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    isbn = db.Column(db.Integer, nullable=False, unique=True)
    titulo = db.Column(db.String(100), nullable=False)
    editora = db.Column(db.String(50), nullable=False)
    quantidade = db.Column(db.Integer, nullable=False)
    autores = db.relationship(
        'Autor',
        secondary=autores,
        backref=db.backref('autores', lazy='dynamic')
    )
    reservas = db.relationship(
        'Reserva',
        backref='livro',
        lazy=True
    )

    def __repr__(self):
        return f'isbn: {self.isbn} titulo: {self.titulo} editora: {self.editora} quantidade: {self.quantidade} autores: {self.autores} reservas: {self.reservas}.'
