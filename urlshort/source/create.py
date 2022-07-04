import json
import os
import random
import string
import boto3

URL_TABLE = os.environ["DYNAMODB_TABLE"]
DNS_RECORD = os.environ["DNS_RECORD"]

dynamodb_client = boto3.client("dynamodb")


def handler(event, context):
    event_body = event.get('body')

    if not event_body:
        return {"statuscode": 400, "body": json.dumps(
            {"error": "body is empty!"})
                }

    request_body = json.loads(event_body)

    long_url = request_body.get("long_url")
    if not long_url:
        return {"statuscode": 400, "body": json.dumps(
            {"error": "param long_url required"})
                }

    url_id = ''.join(random.choices(string.ascii_lowercase + string.digits, k=6))

    dynamodb_client.put_item(
        TableName=URL_TABLE,
        Item={
            "url_id": {"S": url_id},
            "long_url": {"S": long_url}
        }
    )

    short_url = DNS_RECORD + url_id

    response = {
        "StatusCode": 200,
        "body": json.dumps({
            "url_id": url_id,
            "short_url": short_url,
        })
    }

    return response
