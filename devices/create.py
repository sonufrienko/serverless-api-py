import json
import os
import time
import uuid
import boto3
from jsonschema import validate, exceptions

dynamodb = boto3.resource("dynamodb")

item_schema = {
    "type": "object",
    "properties": {"name": {"type": "string", "maxLength": 50},},
    "required": ["name"],
}


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


def validate_body(data: dict):
    try:
        validate(instance=data, schema=item_schema)
    except exceptions.ValidationError as err:
        return err.message


def main(event, context):
    # todo: replace with <token.sub>
    user_id = "sergey.onufrienko"
    data = json.loads(event["body"])

    validation_error = validate_body(data)

    if validation_error:
        return {
            "statusCode": 400,
            "body": json.dumps({"success": False, "errors": [validation_error]}),
        }

    table = dynamodb.Table(os.environ["DEVICES_TABLE"])
    item = get_device_item(user_id, data)
    table.put_item(Item=item)

    response = {"statusCode": 200, "body": json.dumps({"success": True})}

    return response
