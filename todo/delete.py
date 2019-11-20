import os
from logger import logger
from libs.dynamodb import table


def delete(event, context):
    logger.info('event : {event}'.format(event=event))

    params = {
        'TableName': os.environ['TODO_DYNAMODB'],
        'Key': {
            'userId': event['requestContext']['identity']['cognitoIdentityId'],
            'noteId': event['pathParameters']['id']
        }
    }
    result = table(**params).delete_item(**params)

    # TODO : error handling
    # TODO : await -> see serverlessstack
    response = {
        "statusCode": 200
    }

    return response
