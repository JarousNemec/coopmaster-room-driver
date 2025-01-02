import json
import logging
import random
from datetime import datetime

from flask import Blueprint, request, jsonify, make_response

from app.room.room_data_reader import get_weight, get_humidity, get_temperature

room_blueprint = Blueprint('room_blueprint', __name__)


@room_blueprint.route("/api/temperature", methods=['GET'])
def get_temperature_endpoint():
    response = get_temperature()

    response = {'value': random.randint(-5, 40),'unit': "C"}

    return make_response(response)


@room_blueprint.route("/api/humidity", methods=['GET'])
def get_humidity_endpoint():
    response = get_humidity()
    response = {'value': random.randint(50, 100),'unit': '%'}
    return make_response(response)


@room_blueprint.route("/api/lamp/state", methods=['GET'])
def get_lamp_endpoint():
    # response = get_lamp()

    response = "on"
    return make_response(response)


@room_blueprint.route("/api/door/state", methods=['GET'])
def get_door_endpoint():
    # response = get_door()
    response = "open"
    return make_response(response)


@room_blueprint.route("/api/lamp/on", methods=['POST'])
def set_lamp_on_endpoint():
    response = "accepted"
    return make_response(response)

@room_blueprint.route("/api/lamp/off", methods=['POST'])
def set_lamp_of_endpoint():
    response = "accepted"
    return make_response(response)


@room_blueprint.route("/api/door/open", methods=['POST'])
def set_door_open_endpoint():
    response = "refused"
    return make_response(response)


@room_blueprint.route("/api/door/close", methods=['POST'])
def set_door_close_endpoint():
    response = "refused"
    return make_response(response)
