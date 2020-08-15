import json
import os
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource("dynamodb")


def transform_item(pk: str, sk: str, name: str) -> dict:
    return {"device": sk, "name": name}


def transform_list(items: list) -> list:
    return [transform_item(**item) for item in items]


def get_items(user_id):
    table = dynamodb.Table(os.environ["DEVICES_TABLE"])
    result = table.query(Limit=10, KeyConditionExpression=Key("pk").eq(user_id),)
    return transform_list(result["Items"])


def main(event, context):
    # todo: replace with <token.sub>
    items = get_items("sergey.onufrienko")

    response = {"statusCode": 200, "body": json.dumps(items)}

    return response
