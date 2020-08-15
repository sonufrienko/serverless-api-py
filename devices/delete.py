import os
import boto3

dynamodb = boto3.resource("dynamodb")


def delete_device(user_id: str, device: str):
    table = dynamodb.Table(os.environ["DEVICES_TABLE"])
    table.delete_item(Key={"pk": user_id, "sk": device})


def main(event, context):
    # todo: replace with <token.sub>
    user_id = "sergey.onufrienko"
    device = event["pathParameters"]["device"]
    delete_device(user_id, device)

    response = {"statusCode": 200}

    return response
