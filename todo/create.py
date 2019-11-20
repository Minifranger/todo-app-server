import os
import json
import uuid
from logger import logger
from libs.dynamodb import table


def create(event, context):
    logger.info('event : {event}'.format(event=event))

    params = {
        'TableName': os.environ['TODO_DYNAMODB'],
        'Item': {
            'userId': event['requestContext']['identity']['cognitoIdentityId'],
            'noteId': str(uuid.uuid1()),
            'content': str(event['content']),
            'frequency': int(event['frequency'])
        }
    }

    # TODO : async call
    table(**params).put_item(**params)

    # TODO : error handling
    response = {
        "statusCode": 200,
        "body": json.dumps(params['Item'])
    }

    return response
