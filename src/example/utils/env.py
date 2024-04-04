import os
import socket

from dotenv import load_dotenv

load_dotenv()


def get_deployment_name():
    return os.getenv("DEPLOYMENT_NAME", socket.gethostname())
