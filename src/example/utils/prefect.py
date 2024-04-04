import logging
import os
import socket

from dotenv import load_dotenv
from prefect import get_run_logger


def get_logger():
    try:
        return get_run_logger()
    except:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


load_dotenv()


def get_deployment_name():
    return os.getenv("DEPLOYMENT_NAME", socket.gethostname())
