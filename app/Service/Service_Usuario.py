from datetime import datetime

from app import db
from app.Entidades.Usuario import Usuario


class ServiceUsuario:

    @staticmethod
    def save_user(dados):  # post
        usuario = Usuario.query.filter_by(username=dados['username']).first()
        if not usuario:
            novo_usuario = Usuario(
                username=dados['username'],
                nome=dados['nome'],
                email=dados['email'],
                senha=dados['senha'],
                telefone=dados['telefone'],
                data_criacao=datetime.utcnow()
            )
            ServiceUsuario.save(novo_usuario)
            resposta = {
                'status': 'sucesso',
                'message': 'Registro adicionado com sucesso'
            }
            return resposta, 201  # created
        else:
            resposta = {
                'status': 'falha',
                'message': 'Usuário já está cadastrado'
            }
            return resposta, 409

    @staticmethod
    def get_all_users():
        usuarios = Usuario.query.all()
        return usuarios

    @staticmethod
    def get_user_by_id(id):
        usuario = Usuario.query.filter_by(id=id).first()
        if not usuario:
            resposta = {
                'status': 'falha',
                'message': 'Usuário não está cadastrado'
            }
            return resposta, 404
        return usuario

    @staticmethod
    def get_user_by_username(username):
        usuario = Usuario.query.filter_by(username=username).first()
        if not usuario:
            resposta = {
                'status': 'falha',
                'message': 'Usuário não está cadastrado'
            }
            return resposta, 404
        return usuario

    @staticmethod
    def update_user(dados):  # patch, put
        usuario = Usuario.query.filter_by(username=dados['username']).first()
        if usuario:
            usuario.username = dados['username']
            usuario.nome = dados['nome']
            usuario.email = dados['email']
            usuario.senha = dados['senha']
            usuario.telefone = dados['telefone']
            db.session.commit()
            resposta = {
                'status': 'sucesso',
                'message': 'Dados do usuário atualizados.'
            }
            return resposta, 200
        resposta = {
            'status': 'falha',
            'message': 'Usuário não existe. Informe os dados corretamente.'
        }
        return resposta, 404

    @staticmethod
    def delete_user(id):
        usuario = ServiceUsuario.get_user_by_id(id)
        if usuario[1] == 200:
            ServiceUsuario.delete(usuario[0])
            resposta = {
                'status': 'sucesso',
                'message': 'Dados do usuário removidos.'
            }
            return resposta, 200
        resposta = {
            'status': 'falha',
            'message': 'Usuário não existe. Informe os dados corretamente.'
        }
        return resposta, 404

    def save(dados):
        db.session.add(dados)
        db.session.commit()

    def delete(dados):
        db.session.delete(dados)
        db.session.commit()
