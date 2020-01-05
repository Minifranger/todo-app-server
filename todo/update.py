import os
from logger import logger
from utils import dynamodb_table


def update(event, context):
    logger.info('event : {event}'.format(event=event))

    params = {
        'TableName': os.environ['TODO_DYNAMODB'],
        'Key': {'noteId': event['pathParameters']['id']},
        'UpdateExpression': "SET content = :content, frequency = :frequency",
        'ExpressionAttributeValues': {
            ":content": event.get('content', None),
            ":frequency": event.get('frequency', None)
        }
    }

    # TODO : async call
    dynamodb_table(**params).update_item(**params)

    # TODO : error handling
    response = {
        "statusCode": 200
    }

    return response
