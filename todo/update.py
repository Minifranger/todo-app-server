import os
from logger import logger
from libs.dynamodb import table


def update(event, context):
    logger.info('event : {event}'.format(event=event))

    params = {
        'TableName': os.environ['TODO_DYNAMODB'],
        'Key': {
            'userId': event['requestContext']['identity']['cognitoIdentityId'],
            'noteId': event['pathParameters']['id']
        },
        'UpdateExpression': "SET content = :content, frequency = :frequency",
        'ExpressionAttributeValues': {
            ":content": event.get('content', None),
            ":frequency": event.get('frequency', None)
        }
    }
    result = table(**params).update_item(**params)

    # TODO : error handling
    # TODO : await -> see serverlessstack
    response = {
        "statusCode": 200
    }

    return response
