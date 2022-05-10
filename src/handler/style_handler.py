from src.service import style_service
import json


def get_user_styles(event, context):

    user_id = event["pathParameters"]["id"]
    styles = style_service.get_user_styles(user_id)
    response = {"statusCode": 200, "body": json.dumps(styles)}
    return response
