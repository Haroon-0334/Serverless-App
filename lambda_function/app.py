import json
import boto3
import os
import random

dynamodb = boto3.resource("dynamodb")
table = dynamodb.Table("ItemsTable")

def lambda_handler(event, context):
    body = json.loads(event.get("body", "{}"))
    item_id = random.randint(1, 1000000)  # generates a number between 1 and 1,000,000
    item_name = body.get("name", "default_name")

    table.put_item(Item={"item_id": item_id, "name": item_name})


    return {
    "statusCode": 200,
    "headers": {
        "Access-Control-Allow-Origin": "*",
        "Access-Control-Allow-Methods": "OPTIONS,POST,GET",
        "Access-Control-Allow-Headers": "Content-Type"
    },
    "body": json.dumps({"item_id": item_id, "name": item_name})
}

