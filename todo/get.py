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

    # TODO : async call
    result = table(**params).get_item(**params)

    # TODO : error handling
    if result.get('Item'):
        response = {
            "statusCode": 200,
            "body": json.dumps(result.get('Item'), cls=DecimalEncoder)
        }
        return response
    else:
        raise KeyError('Item not found')

