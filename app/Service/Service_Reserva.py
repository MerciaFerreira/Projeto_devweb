from datetime import datetime

from app import db
from app.Entidades.Reserva import Reserva
from app.Service.Service_Usuario import ServiceUsuario
from app.Service.Service_Livro import ServiceLivro


class ServiceReserva:

    @staticmethod
    def save_reserva(dados):  # username, isbn
        usuario = ServiceUsuario.get_usuario_by_username(dados['username'])
        livro = ServiceLivro.get_livro_by_isbn(dados['isbn'])
        if usuario and livro:
            reserva = Reserva.query.filter(
                Reserva.usuario_id == usuario.id,
                Reserva.livro_id == livro.id,
                Reserva.data_vencimento >= datetime.utcnow()
            ).first()
            if not reserva:
                nova_reserva = Reserva(
                    data_emprestimo=datetime.utcnow(),
                    data_vencimento=datetime.strptime(dados['data_vencimento'], '%Y/%m/%d')  # 2020/09/01
                )
                nova_reserva.usuario = usuario
                nova_reserva.livro = livro
                ServiceReserva.save(nova_reserva)
                return nova_reserva

    @staticmethod
    def get_all_reservas():
        reservas = Reserva.query.all()
        return reservas

    @staticmethod
    def get_reserva_by_id(id):
        reserva = Reserva.query.get(id)
        return reserva

    @staticmethod
    def update_reserva(id, dados):
        reserva = Reserva.query.get(id)
        if reserva:
            reserva.data_vencimento = datetime.strptime(dados['data_vencimento'], '%Y/%m/%d')
            return reserva

    @staticmethod
    def delete_reserva(id):
        reserva = Reserva.query.get(id)
        if reserva:
            ServiceReserva.delete(reserva)
            return reserva

    def save(dados):
        db.session.add(dados)
        db.session.commit()

    def delete(dados):
        db.session.delete(dados)
        db.session.commit()
