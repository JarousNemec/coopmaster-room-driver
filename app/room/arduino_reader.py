import threading
import serial
import logging
import time

from app import configuration


class ArduinoReader:

    def __init__(self):
        self.arduino = serial.Serial(
            port=configuration.config.ROOM_COM_PORT,
            baudrate=9600,
            timeout=1
        )
        self.lock = threading.Lock()
        self.run_command('j')

    def run_command(self, command):
        with self.lock:
            try:
                if self.arduino:
                    try:
                        self.arduino.readall()
                        self.arduino.write(command.encode('ascii'))
                        str_data = self.arduino.readline().decode('ascii')
                        logging.info(str_data)
                        return str_data
                    except Exception as ex:
                        logging.exception(ex)
                else:
                    logging.error("Arduion neni")
            except Exception as ex:
                # if permission denied occurred, try
                # "sudo usermod -a -G tty yourname"

                logging.exception(ex)
