from flask import request, jsonify, Blueprint
from ..Service.Service_Autor import ServiceAutor
from ..Entidades.Autor import autor_schema, autores_schema

autor_blueprint = Blueprint('autores', __name__)


@autor_blueprint.route('/autores', methods=['GET'])
def get_all_autores():
    return autores_schema.jsonify(ServiceAutor.get_all_autores())


@autor_blueprint.route('/autores/<int:autor_id>', methods=['GET'])
def get_autores(autor_id):
    return autor_schema.jsonify(ServiceAutor.get_autor_by_id(autor_id))


@autor_blueprint.route('/autores', methods=['POST'])
def create_autor():
    return autor_schema.jsonify(ServiceAutor.save_autor(request.get_json()))


@autor_blueprint.route('/autores/<int:autor_id>', methods=['PUT'])
def update_autor(autor_id):
    return autor_schema.jsonify(ServiceAutor.update_autor(autor_id, request.get_json()))


@autor_blueprint.route('/autores/<int:autor_id>', methods=['DELETE'])
def delete_autor(autor_id):
    return autor_schema.jsonify(ServiceAutor.delete_autor(autor_id))
