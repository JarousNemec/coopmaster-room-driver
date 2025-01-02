import json
from flask import Blueprint, make_response

from app.configuration import arduino

room_blueprint = Blueprint('room_blueprint', __name__)


@room_blueprint.route("/api/temperature", methods=['GET'])
def get_temperature_endpoint():
    value = json.loads(arduino.run_command('j'))["temperature"]
    response = {'value': value, 'unit': "C"}
    return make_response(response)


@room_blueprint.route("/api/humidity", methods=['GET'])
def get_humidity_endpoint():
    value = json.loads(arduino.run_command('j'))["humidity"]
    response = {'value': value, 'unit': '%'}
    return make_response(response)


@room_blueprint.route("/api/lamp/state", methods=['GET'])
def get_lamp_endpoint():
    response = json.loads(arduino.run_command('s'))["lamp"]
    return make_response(response)


@room_blueprint.route("/api/door/state", methods=['GET'])
def get_door_endpoint():
    response = json.loads(arduino.run_command('s'))["door"]
    return make_response(response)


@room_blueprint.route("/api/lamp/on", methods=['POST'])
def set_lamp_on_endpoint():
    arduino.run_command('l')
    response = "accepted"
    return make_response(response)


@room_blueprint.route("/api/lamp/off", methods=['POST'])
def set_lamp_off_endpoint():
    arduino.run_command('d')
    response = "accepted"
    return make_response(response)


@room_blueprint.route("/api/door/open", methods=['POST'])
def set_door_open_endpoint():
    arduino.run_command('o')
    response = "accepted"
    return make_response(response)


@room_blueprint.route("/api/door/close", methods=['POST'])
def set_door_close_endpoint():
    arduino.run_command('c')
    response = "accepted"
    return make_response(response)
