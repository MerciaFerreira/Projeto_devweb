from datetime import datetime

from app import db
from app.Entidades.Reserva import Reserva
from app.Service.Service_Usuario import ServiceUsuario
from app.Service.Service_Livro import ServiceLivro


class ServiceReserva:

    @staticmethod
    def save_reserva(dados):  # username, isbn
        usuario = ServiceUsuario.get_user_by_username(dados['username'])
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
                resposta = {
                    'status': 'sucesso',
                    'message': 'Reserva registrada no sistema.'
                }
                return resposta, 201
        if not usuario:
            resposta = {
                'status': 'falha',
                'message': 'Username inválido.'
            }
            return resposta, 201
        if not livro:
            resposta = {
                'status': 'falha',
                'message': 'ISBN não encontrado no sistema.'
            }
            return resposta, 201

    @staticmethod
    def get_all_reservas():
        reservas = Reserva.query.all()
        return reservas

    @staticmethod
    def get_reserva_by_id(id):
        reserva = Reserva.query.get(id)
        return reserva

    @staticmethod
    def update_reserva(dados):
        pass

    @staticmethod
    def delete_reserva(id):
        pass

    def save(dados):
        db.session.add(dados)
        db.session.commit()

    def delete(dados):
        db.session.delete(dados)
        db.session.commit()
