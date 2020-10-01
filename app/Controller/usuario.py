from flask import request, jsonify, Blueprint
from ..Service.Service_Usuario import ServiceUsuario
from ..Entidades.Usuario import usuario_schema, usuarios_schema

usuario_blueprint = Blueprint('usuarios', __name__)


@usuario_blueprint.route('/usuarios', methods=['GET'])
def get_all_usuarios():
    return usuarios_schema.jsonify(ServiceUsuario.get_all_usuarios())


@usuario_blueprint.route('/usuarios/<int:usuario_id>', methods=['GET'])
def get_usuario(usuario_id):
    return usuario_schema.jsonify(ServiceUsuario.get_usuario_by_id(usuario_id))


@usuario_blueprint.route('/usuarios', methods=['POST'])
def create_usuario():
    return usuario_schema.jsonify(ServiceUsuario.save_usuario(request.get_json()))


@usuario_blueprint.route('/usuarios/<int:usuario_id>', methods=['PUT'])
def update_usuario(usuario_id):
    return usuario_schema.jsonify(ServiceUsuario.update_usuario(usuario_id, request.get_json()))


@usuario_blueprint.route('/usuarios/<int:usuario_id>', methods=['DELETE'])
def delete_usuario(usuario_id):
    return usuario_schema.jsonify(ServiceUsuario.delete_usuario(usuario_id))
