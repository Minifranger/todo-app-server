import os
import json
from logger import logger
from libs.dynamodb import table
from utils import DecimalEncoder


def get(event, context):
    logger.info('event : {event}'.format(event=event))

    params = {
        'TableName': os.environ['TODO_DYNAMODB'],
        'Key': {
            'userId': event['requestContext']['identity']['cognitoIdentityId'],
            'noteId': event['pathParameters']['id']
        }
    }

    item = table(**params).get_item(**params).get('Item')

    # TODO : error handling
    # TODO : await -> see serverlessstack
    if item:
        response = {
            "statusCode": 200,
            "body": json.dumps(item, cls=DecimalEncoder)
        }
        return response
    else:
        raise KeyError('Item not found')

