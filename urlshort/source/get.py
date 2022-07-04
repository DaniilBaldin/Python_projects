import json
import os
import boto3


URL_TABLE = os.environ["DYNAMODB_TABLE"]
DNS_RECORD = os.environ['DNS_RECORD']

dynamodb_client = boto3.client("dynamodb")


def handler(event, context):
    url_id = event["pathParameters"]["url_id"]

    result = dynamodb_client.get_item(
        TableName=URL_TABLE,
        Key={"url_id": {"S": url_id}}).get("Item")

    if not result:
        return {"statuscode": 404, "body": json.dumps(
            {"error": "URL not found"})
                }

    long_url = result.get("long_url").get("S")

    response = {
        "headers": {"Location": long_url},
        "statuscode": 301,
    }

    return response
