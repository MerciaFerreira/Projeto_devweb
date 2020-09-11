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
            resposta = {
                'status': 'sucesso',
                'message': 'Registro adicionado com sucesso'
            }
            return resposta, 201  # created
        else:
            resposta = {
                'status': 'falha',
                'message': 'Autor já está cadastrado'
            }
        return resposta, 409

    @staticmethod
    def get_all_autores():
        pass

    @staticmethod
    def get_autor_by_id(id):
        autor = Autor.query.get(id)
        return autor

    @staticmethod
    def get_autor_by_nome(id):
        pass

    @staticmethod
    def get_autor_by_sobrenome(id):
        pass

    @staticmethod
    def update_autor(dados):
        pass

    @staticmethod
    def delete_autor(id):
        pass

    def save(dados):
        db.session.add(dados)
        db.session.commit()

    def delete(dados):
        db.session.delete(dados)
        db.session.commit()
