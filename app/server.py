import logging

from flask import Flask
from waitress import serve

from app import configuration
from app.blueprints.admin_blueprint import admin_blueprint
from app.blueprints.room_blueprint import room_blueprint
from app.room.room_data_reader import start_gobbler


def flask_app():
    app = Flask('__main__')

    @app.route("/")
    def hello_world():
        message = 'Hello from room driver'
        logging.info(message)
        return message

    app.register_blueprint(admin_blueprint)
    app.register_blueprint(room_blueprint)

    return app


def server():
    manager_app = flask_app()

    start_gobbler()

    host = configuration.config.HOST
    port = configuration.config.PORT

    logging.info(f"Serving on http://{host}:{port}")
    serve(manager_app,  port=port)
