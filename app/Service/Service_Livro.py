from app import db
from app.Entidades.Livro import Livro
from app.Service.Service_Autor import ServiceAutor


class ServiceLivro:

    @staticmethod
    def save_livro(dados):
        livro = Livro.query.filter_by(isbn=dados['isbn']).first()
        if not livro:
            novo_livro = Livro(
                isbn=dados['isbn'],
                titulo=dados['titulo'],
                editora=dados['editora'],
                quantidade=dados['quantidade']
            )
            [novo_livro.autores.append(obj) for obj in
                [ServiceAutor.get_autor_by_id(autor) for autor in
                    dados['autores']]]
            ServiceLivro.save(novo_livro)
            return novo_livro

    @staticmethod
    def get_all_livros():
        livros = Livro.query.all()
        return livros

    @staticmethod
    def get_livro_by_id(id):
        livro = Livro.query.get(id)
        return livro

    @staticmethod
    def get_livro_by_isbn(isbn):
        livro = Livro.query.filter_by(isbn=isbn).first()
        return livro

    def get_livros_by_autor(dados):
        autor = ServiceAutor.get_autor_by_id(dados['id'])
        livros = Livro.query.with_parent(autor).all()
        return livros

    @staticmethod
    def update_livro(id, dados):
        livro = Livro.query.get(id)
        if livro:
            livro.isbn = dados['isbn']
            livro.titulo = dados['titulo']
            livro.editora = dados['editora']
            livro.quantidade = dados['quantidade']
            db.session.commit()
            return livro

    @staticmethod
    def delete_livro(id):
        livro = Livro.query.get(id)
        if livro:
            ServiceLivro.delete(livro)
            return livro

    def save(dados):
        db.session.add(dados)
        db.session.commit()

    def delete(dados):
        db.session.delete(dados)
        db.session.commit()

#outra forma de fazer mas melhor a que já tá
#linha 18 - 21
           # for autor in dados['autores']:
            #     autor_encontrado = ServiceAutor.get_autor_by_id(autor)
            #     if autor:
            #         novo_livro.autores.append(autor_encontrado)