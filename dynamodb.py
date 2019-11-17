import os
import boto3

dynamodb = boto3.resource('dynamodb')
todo_table = dynamodb.Table(os.environ['TODO_DYNAMODB'])
