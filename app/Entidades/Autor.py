from app import db, ma


class Autor(db.Model):

    __tablename__ = 'autor'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    sobrenome = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'nome: {self.nome} sobrenome: {self.sobrenome}.'


class AutorSchema(ma.Schema):
    class Meta:
        model = Autor
        fields = ('id', 'nome', 'sobrenome')


autor_schema = AutorSchema()
autores_schema = AutorSchema(many=True)
