import os
import json
from logger import logger
from libs.dynamodb import table
from utils import DecimalEncoder


def list_note(event, context):
    logger.info('event : {event}'.format(event=event))

    params = {
        'TableName': os.environ['TODO_DYNAMODB'],
        'KeyConditionExpression': 'userId = :userId',
        'ExpressionAttributeValues': {
            ":userId": event['requestContext']['identity']['cognitoIdentityId']
        }
    }

    result = table(**params).query(**params)

    # TODO : error handling
    # TODO : await -> see serverlessstack
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=DecimalEncoder)
    }
    return response
