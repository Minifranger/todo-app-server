import os
import json
import uuid
from logger import logger
from utils import dynamodb_table


def create(event, context):
    logger.info('event : {event}'.format(event=event))

    params = {
        'TableName': os.environ['TODO_DYNAMODB'],
        'Item': {
            'noteId': str(uuid.uuid1()),
            'content': str(event['content']),
            'frequency': int(event['frequency'])
        }
    }

    # TODO : async call
    dynamodb_table(**params).put_item(**params)

    # TODO : error handling
    response = {
        "statusCode": 200,
        "body": json.dumps(params['Item'])
    }

    return response
