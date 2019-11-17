import json
import uuid
from dynamodb import todo_table
from logger import logger


def create(event, context):
    logger.info('event : {event}'.format(event=event))

    params = {
        'Item': {
            'userId': event['requestContext']['identity']['cognitoIdentityId'],
            'noteId': str(uuid.uuid1()),
            'content': str(event['content']),
            'frequency': int(event['frequency'])
        }
    }

    todo_table.put_item(**params)

    # TODO : error handling
    # TODO : await -> see serverlessstack
    response = {
        "statusCode": 200,
        "body": json.dumps(params['Item'])
    }

    return response
