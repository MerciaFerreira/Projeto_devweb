from app import create_app, db

from app.Service.Service_Usuario import ServiceUsuario

app = create_app('config')

usuarios = [
    {  # 0
        'username': 'matto96',
        'nome': 'Matheus',
        'email': 'matheus@email.com',  # regex email python
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

if name == 'main':
    with app.app_context():
        db.drop_all()
        db.create_all()
        print('[+] Database created')
        [ServiceUsuario.save_user(usuario) for usuario in usuarios]
        print('[+] Usuarios created')
        # us = Serget_all_users()
        # print(us)
        us = ServiceUsuario.get_user_by_id(5)
        print(us)

        ServiceUsuario.update_user(update_lucas)

        us = ServiceUsuario.get_user_by_id(2)
        print(us)

        us = ServiceUsuario.delete_user(2)
        print(us)

        us = ServiceUsuario.get_user_by_id(2)
        print(us)