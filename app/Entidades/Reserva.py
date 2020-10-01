from app import db, ma


class Reserva(db.Model):

    __tablename__ = 'reserva'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    data_emprestimo = db.Column(db.Date, nullable=False)
    data_vencimento = db.Column(db.Date, nullable=False)
    usuario_id = db.Column(
        db.Integer,
        db.ForeignKey('usuario.id'),
        nullable=False
    )
    livro_id = db.Column(
        db.Integer,
        db.ForeignKey('livro.id'),
        nullable=False
    )


class ReservaSchema(ma.Schema):
    class Meta:
        model = Reserva
        fields = (
            'id',
            'data_emprestimo',
            'data_vencimento',
            'usuario_id',
            'livro_id'
        )


reserva_schema = ReservaSchema()
reservas_schema = ReservaSchema(many=True)
