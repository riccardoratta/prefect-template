import logging
from prefect import get_run_logger


def get_logger():
    try:
        return get_run_logger()
    except:
        logger = logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
