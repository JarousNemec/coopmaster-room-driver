import json
import logging
from datetime import datetime

from flask import Blueprint, request, jsonify, make_response

from app.room.room_data_reader import get_weight, get_humidity, get_temperature

room_blueprint = Blueprint('room_blueprint', __name__)


@room_blueprint.route("/api/temperature", methods=['GET'])
def get_temperature_endpoint():
    response = get_temperature()
    return make_response(response)


@room_blueprint.route("/api/humidity", methods=['GET'])
def get_humidity_endpoint():
    response = get_humidity()
    return make_response(response)