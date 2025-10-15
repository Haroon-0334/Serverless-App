import json
import boto3
import os
import uuid

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("ItemsTable")

def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))
    item_id = str(uuid.uuid4())
    item_name = body.get("name", "default_name")

    table.put_item(Item={"item_id": item_id, "name": item_name})

    return {
        "statusCode": 200,
        "body": json.dumps({"item_id": item_id, "name": item_name})
    }
