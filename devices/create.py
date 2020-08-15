import json
import os
import time
import uuid

import boto3

dynamodb = boto3.resource("dynamodb")


def get_device_item(user_id, data: dict) -> dict:
    timestamp = str(time.time())

    item = {
        "pk": user_id,
        "sk": str(uuid.uuid1()),
        "name": data["name"],
        "createdAt": timestamp,
        "updatedAt": timestamp,
    }

    return item


def main(event, context):
    # todo: replace with <token.sub>
    user_id = "sergey.onufrienko"
    data = json.loads(event["body"])

    if "name" not in data:
        raise Exception("Missing field - name")

    table = dynamodb.Table(os.environ["DEVICES_TABLE"])
    item = get_device_item(user_id, data)
    table.put_item(Item=item)

    response = {"statusCode": 200, "body": json.dumps({"success": True})}

    return response
