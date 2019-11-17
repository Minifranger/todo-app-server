import logging

logger = logging.getLogger(__name__)
""" AWS Lambda only logs error, change for dev """
logger.setLevel(logging.INFO)