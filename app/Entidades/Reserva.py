from app import db


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

    def __repr__(self):
        return f'data_emprestimo: {self.data_emprestimo} data_vencimento: {self.data_vencimento} usuario_id: {self.usuario_id} livro_id: {self.livro_id}.'
