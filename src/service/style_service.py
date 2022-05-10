import os
from src.service.dynamo import dynamo_service

table = os.environ["STYLES_TABLE"]


def get_user_styles(user_id):
    return dynamo_service.get_user_styles(user_id, table)
