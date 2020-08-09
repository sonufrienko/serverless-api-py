import json
import os
import boto3

dynamodb = boto3.resource("dynamodb")


def main(event, context):
    httpContext = event["requestContext"]["http"]

    table = dynamodb.Table(os.environ["DEVICES_TABLE"])

    # fetch all todos from the database
    result = table.scan()

    response = {"statusCode": 200, "body": json.dumps(result["Items"])}

    return response
