from datetime import datetime

from app import db
from app.Entidades.Usuario import Usuario


class ServiceUsuario:

    @staticmethod
    def save_usuario(dados):  # post
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
            return novo_usuario

    @staticmethod
    def get_all_usuarios():
        usuarios = Usuario.query.all()
        return usuarios

    @staticmethod
    def get_usuario_by_id(id):
        usuario = Usuario.query.filter_by(id=id).first()
        return usuario

    @staticmethod
    def get_usuario_by_username(username):
        usuario = Usuario.query.filter_by(username=username).first()
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
            return usuario

    @staticmethod
    def delete_usuario(id):
        usuario = Usuario.query.get(id)
        if usuario:
            delete(usuario)
            return usuario

    def save(dados):
        db.session.add(dados)
        db.session.commit()

    def delete(dados):
        db.session.delete(dados)
        db.session.commit()
