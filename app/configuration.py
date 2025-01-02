import os
from typing import get_type_hints, Union

from dotenv import load_dotenv

from app.room.arduino_reader import ArduinoReader

host = "127.0.0.1"
port = 9005
hello_message = "Hello from door driver"

log_file_name = "door_driver.log"

load_dotenv()


def _parse_bool(val: Union[str, bool]) -> bool:  # pylint: disable=E1136
    return val if type(val) == bool else val.lower() in ['true', 'yes', '1']


class AppConfigError(Exception):
    pass


class AppConfig:
    PORT: int = 29005
    HOST: str = "127.0.0.1"
    ROOM_COM_PORT = "COM4"
    # ROOM_COM_PORT: str = "/dev/ttyUSB0"  # linux Ubuntu wth weight Arduino 'COM4'
    ROOM_READ_INTERVAL_SEC: int = 1
    ROOM_COMMAND_INTERVAL_SEC: int = 5


    """
    Map environment variables to class fields according to these rules:
      - Field won't be parsed unless it has a type annotation
      - Field will be skipped if not in all caps
      - Class field and environment variable name are the same
    """

    def __init__(self, env):

        for field in self.__annotations__:
            if not field.isupper():
                continue

            # Raise AppConfigError if required field not supplied
            default_value = getattr(self, field, None)
            if default_value is None and env.get(field) is None:
                raise AppConfigError('The {} field is required'.format(field))

            # Cast env var value to expected type and raise AppConfigError on failure
            try:
                var_type = get_type_hints(AppConfig)[field]
                if var_type == bool:
                    value = _parse_bool(env.get(field, default_value))
                else:
                    value = var_type(env.get(field, default_value))

                self.__setattr__(field, value)
            except ValueError:
                raise AppConfigError('Unable to cast value of "{}" to type "{}" for "{}" field'.format(
                    env[field],
                    var_type,
                    field
                )
                )

    def __repr__(self):
        return str(self.__dict__)


config = AppConfig(os.environ)
arduino = ArduinoReader()

def get_log_directory():
    return "./logs/"

def get_log_filename():
    return log_file_name