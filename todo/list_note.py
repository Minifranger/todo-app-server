import os
import json
from logger import logger
from utils import DecimalEncoder, dynamodb_table


def list_note(event, context):
    logger.info('event : {event}'.format(event=event))

    params = {
        'TableName': os.environ['TODO_DYNAMODB']
        # 'KeyConditionExpression': 'userId = :userId',
        # 'ExpressionAttributeValues': {
        #     ":userId": event['requestContext']['identity']['cognitoIdentityId']
        # }
    }

    # TODO : async call
    result = dynamodb_table(**params).scan()

    # TODO : error handling
    response = {
        "statusCode": 200,
        "body": json.dumps(result['Items'], cls=DecimalEncoder)
    }
    return response
