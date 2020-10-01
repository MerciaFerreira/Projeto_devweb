from app import create_app, db

from app.Service.Service_Usuario import ServiceUsuario
from app.Service.Service_Autor import ServiceAutor
from app.Service.Service_Livro import ServiceLivro
from app.Service.Service_Reserva import ServiceReserva

app = create_app('config')


usuarios = [
    {  # 0
        'username': 'jamille10',
        'nome': 'Jamille',
        'email': 'jamille@email.com',  # regex email python
        'senha': '123456',
        'telefone': '88999999999'
    },
    {  # 1
        'username': 'lucaslpx',
        'nome': 'Luxas',
        'email': 'lucas@email.com',  # regex email python
        'senha': '654321',
        'telefone': '888568974611'
    },
    {  # 2
        'username': 'mercia2020',
        'nome': 'Mercia',
        'email': 'mercia@email.com',  # regex email python
        'senha': 'teste123456',
        'telefone': '888568975555'
    }
]


update_lucas = {
        'username': '',
        'nome': '',
        'email': 'lucaslucasmudado@email.com',  # regex email python
        'senha': '111111111',
        'telefone': '888568974611'
}


autores = [
    {
        'nome': 'autor1',
        'sobrenome': 'sobrenome1',
    },
    {
        'nome': 'autor2',
        'sobrenome': 'sobrenome2',
    },
    {
        'nome': 'autor3',
        'sobrenome': 'sobrenome3',
    }
]

livros = [
    {
        'isbn': 111111111,
        'titulo': 'livro1',
        'editora': 'editora1',
        'quantidade': 8,
        'autores': [1, 3]
    },
    {
        'isbn': 2222222,
        'titulo': 'livro2',
        'editora': 'editora2',
        'quantidade': 4,
        'autores': [2]
    },
    {
        'isbn': 33333333,
        'titulo': 'livro3',
        'editora': 'editora3',
        'quantidade': 11,
        'autores': [1, 2, 3]
    },
    {
        'isbn': 44444444,
        'titulo': 'livro4',
        'editora': 'editora4',
        'quantidade': 20,
        'autores': [2, 3]
    }
]

reservas = [
    {
        'username': 'jamille10',
        'isbn': 44444444,
        'data_vencimento': '2020/07/15'
    },
    {
        'username': 'mercia2020',
        'isbn': 33333333,
        'data_vencimento': '2020/08/23'
    }
]

if __name__ == '__main__':
    with app.app_context():
        db.drop_all()
        db.create_all()
        print('[+] Database created')
        [ServiceUsuario.save_usuario(usuario) for usuario in usuarios]
        print('[+] Usuarios created')
        [ServiceAutor.save_autor(autor) for autor in autores]
        print('[+] Autores created')
        [ServiceLivro.save_livro(livro) for livro in livros]
        print('[+] Livros created')
        [ServiceReserva.save_reserva(reserva) for reserva in reservas]
        print('[+] Reservas created')

        # reser = ServiceReserva.get_all_reservas()
        # print(reser)

        # usr = ServiceUsuario.get_user_by_username('mercia2020')
        # print(usr)

        lvr = ServiceLivro.get_livro_by_isbn(44444444)
        print(lvr)

        # livrs = ServiceLivro.get_all_livros()
        # print(livrs)

        # livros_autor = ServiceLivro.get_livros_by_autor({'id': 1})
        # print(livros_autor)

        # us = ServiceUsuario.get_user_by_id(5)
        # print(us)

        # ServiceUsuario.update_user(update_lucas)

        # us = ServiceUsuario.get_user_by_id(2)
        # print(us)

        # us = ServiceUsuario.delete_user(2)
        # print(us)

        # us = ServiceUsuario.get_user_by_id(2)
        # print(us)