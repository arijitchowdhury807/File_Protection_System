import logging
import os

# Create logs directory if not exists
os.makedirs(
    "data/logs",
    exist_ok=True
)

logging.basicConfig(
    filename="data/logs/security.log",
    level=logging.INFO,
    format="%(asctime)s - %(message)s"
)


def write_log(message):
    """
    Write security events to log file.
    """

    logging.info(message)