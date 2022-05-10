import boto3
from boto3.dynamodb.conditions import Key
import os

from src.service.dynamo.adapter.style_adapter import toModel

dynamodb = (
    boto3.resource("dynamodb", endpoint_url="http://localhost:8000")
    if os.getenv("IS_OFFLINE")
    else boto3.resource("dynamodb")
)


def get_user_styles(user_id, table_name):
    table = dynamodb.Table(table_name)

    style_dtos = table.query(
        TableName=table_name, KeyConditionExpression=Key("PK").eq(f"USER#${user_id}") & Key("SK").begins_with("STYLE")
    )["Items"]
    return list(map(lambda x: toModel(x), style_dtos))
