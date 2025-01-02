from app.logging.hen_logger import init_logger
from app.server import server

init_logger()


def start_server():
    server()


if __name__ == '__main__':
    print("Hello from room driver")
    start_server()
