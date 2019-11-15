import os
import json
import uuid
import boto3

dynamodb = boto3.resource('dynamodb')


def create(event, context):
    data = json.loads(event['body'])

    table = dynamodb.Table(os.environ['DYNAMODB_TABLE'])

    # TODO : add frequency
    # TODO : change userId
    item = {
        'userId': 'Minifranger',
        'noteId': str(uuid.uuid1()),
        'content': data['content'],
    }

    table.put_item(Item=item)

    # TODO : error handling
    # TODO : await -> see serverlessstack
    response = {
        "statusCode": 200,
        "body": json.dumps(item)
    }

    return response
