from flask import request, jsonify, Blueprint
from ..Service.Service_Reserva import ServiceReserva
from ..Entidades.Reserva import reserva_schema, reservas_schema

reserva_blueprint = Blueprint('reservas', __name__)


@reserva_blueprint.route('/reservas', methods=['GET'])
def get_all_reservas():
    return reservas_schema.jsonify(ServiceReserva.get_all_reservas())


@reserva_blueprint.route('/reservas/<int:reserva_id>', methods=['GET'])
def get_reserva(reserva_id):
    return reserva_schema.jsonify(ServiceReserva.get_reserva_by_id(reserva_id))


@reserva_blueprint.route('/reservas', methods=['POST'])
def create_reserva():
    return reserva_schema.jsonify(ServiceReserva.save_reserva(request.get_json()))


@reserva_blueprint.route('/reservas/<int:reserva_id>', methods=['PUT'])
def update_reserva(reserva_id):
    return reserva_schema.jsonify(ServiceReserva.update_reserva(reserva_id, request.get_json()))


@reserva_blueprint.route('/reservas/<int:reserva_id>', methods=['DELETE'])
def delete_reserva(reserva_id):
    return reserva_schema.jsonify(ServiceReserva.delete_reserva(reserva_id))
