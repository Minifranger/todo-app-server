import boto3


def table(**kwargs):
    return boto3.resource('dynamodb').Table(kwargs.get('TableName', None))
