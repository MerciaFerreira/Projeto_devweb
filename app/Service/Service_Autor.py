from app import db
from app.Entidades.Autor import Autor


class ServiceAutor:

    @staticmethod
    def save_autor(dados):
        autor = Autor.query.filter(
            Autor.nome == dados['nome'],
            Autor.sobrenome == dados['sobrenome']
        ).first()
        if not autor:
            novo_autor = Autor(
                nome=dados['nome'],
                sobrenome=dados['sobrenome']
            )
            ServiceAutor.save(novo_autor)
            return novo_autor

    @staticmethod
    def get_all_autores():
        autores = Autor.query.all()
        return autores

    @staticmethod
    def get_autor_by_id(id):
        autor = Autor.query.get(id)
        return autor

    @staticmethod
    def get_autor_by_nome(nome):
        autores = Autor.query.filter_by(nome=nome).all()
        return autores

    @staticmethod
    def get_autor_by_sobrenome(sobrenome):
        autores = Autor.query.filter_by(sobrenome=sobrenome).all()
        return autores

    @staticmethod
    def update_autor(id, dados):
        autor = Autor.query.get(id)
        if autor:
            autor.nome = dados['nome']
            autor.sobrenome = dados['sobrenome']
            db.session.commit()
            return autor

    @staticmethod
    def delete_autor(id):
        autor = Autor.query.get(id)
        if autor:
            ServiceAutor.delete(autor)
            return autor

    def save(dados):
        db.session.add(dados)
        db.session.commit()

    def delete(dados):
        db.session.delete(dados)
        db.session.commit()
