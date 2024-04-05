import logging
import os
import socket

import toml
from dotenv import load_dotenv
from prefect import get_run_logger


def get_logger():
    try:
        return get_run_logger()
    except:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger


def get_deployment_name():
    load_dotenv()
    return os.getenv("DEPLOYMENT_NAME", socket.gethostname())


def get_version() -> str:
    with open("pyproject.toml", "r") as reader:
        return toml.load(reader)["project"]["version"]
