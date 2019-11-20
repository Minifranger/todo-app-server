import os
from logger import logger
from utils import dynamodb_table


def delete(event, context):
    logger.info('event : {event}'.format(event=event))

    params = {
        'TableName': os.environ['TODO_DYNAMODB'],
        'Key': {
            'userId': event['requestContext']['identity']['cognitoIdentityId'],
            'noteId': event['pathParameters']['id']
        }
    }

    # TODO : async call
    dynamodb_table(**params).delete_item(**params)

    # TODO : error handling
    response = {
        "statusCode": 200
    }

    return response
