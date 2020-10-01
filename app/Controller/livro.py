from flask import request, jsonify, Blueprint
from ..Service.Service_Livro import ServiceLivro
from ..Entidades.Livro import livro_schema, livros_schema

livro_blueprint = Blueprint('livros', __name__)


@livro_blueprint.route('/livros', methods=['GET'])
def get_all_livros():
    return livros_schema.jsonify(ServiceLivro.get_all_livros())


@livro_blueprint.route('/livros/<int:livro_id>', methods=['GET'])
def get_livro(livro_id):
    return livro_schema.jsonify(ServiceLivro.get_livro_by_id(livro_id))


@livro_blueprint.route('/livros', methods=['POST'])
def create_livro():
    return livro_schema.jsonify(ServiceLivro.save_livro(request.get_json()))


@livro_blueprint.route('/livros/<int:livro_id>', methods=['PUT'])
def update_livro(livro_id):
    return livro_schema.jsonify(ServiceLivro.update_livro(livro_id, request.get_json()))


@livro_blueprint.route('/livros/<int:livro_id>', methods=['DELETE'])
def delete_livro(livro_id):
    return livro_schema.jsonify(ServiceLivro.delete_livro(livro_id))
