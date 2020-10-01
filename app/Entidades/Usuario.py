from app import db, ma, bcrypt
from .Reserva import ReservaSchema


class Usuario(db.Model):

    __tablename__ = 'usuario'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    admin = db.Column(db.Boolean, nullable=False, default=False)
    username = db.Column(db.String(50), unique=True, nullable=False)
    senha_hash = db.Column(db.String(100))
    nome = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    telefone = db.Column(db.String(50), unique=True, nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False)
    reservas = db.relationship(

        'Reserva',
        cascade='all, delete',
        backref='usuario',
        lazy=True
    )


    @property
    def senha(self):
        raise AttributeError('senha: não é permitido visualizar')

    @senha.setter
    def senha(self, senha):
        self.senha_hash = bcrypt.generate_password_hash(senha).decode('utf-8')

    def check_senha(self, senha):
        return bcrypt.check_password_hash(self.senha_hash, senha)


class UsuarioSchema(ma.Schema):
    reservas = ma.List(ma.Nested(ReservaSchema))

    class Meta:
        model = Usuario
        fields = (
            'id',
            'admin',
            'username',
            'nome',
            'email',
            'telefone',
            'data_criacao',
            'reservas'
        )


usuario_schema = UsuarioSchema()
usuarios_schema = UsuarioSchema(many=True)
