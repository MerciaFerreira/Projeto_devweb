from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_marshmallow import Marshmallow


db = SQLAlchemy()
ma = Marshmallow()
bcrypt = Bcrypt()

from .Controller.autor import autor_blueprint
from .Controller.livro import livro_blueprint
from .Controller.usuario import usuario_blueprint
from .Controller.reserva import reserva_blueprint


def create_app(config_object):
    app = Flask(__name__)
    app.config.from_object(config_object)

    db.init_app(app)
    ma.init_app(app)
    bcrypt.init_app(app)

    app.register_blueprint(autor_blueprint)
    app.register_blueprint(livro_blueprint)
    app.register_blueprint(usuario_blueprint)
    app.register_blueprint(reserva_blueprint)

    return app
