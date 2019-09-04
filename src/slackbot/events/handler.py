import json
import os
import sys

sys.path.insert(0, os.path.abspath("./src"))

from common.common import common_thing

def endpoint(event, context):
    body = {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "common": common_thing(),
        "input": sys.path,
        "dot": os.path.abspath(".")
    }

    response = {
        "statusCode": 200,
        "body": json.dumps(body)
    }

    return response

    # Use this code if you don't use the http event with the LAMBDA-PROXY
    # integration
    """
    return {
        "message": "Go Serverless v1.0! Your function executed successfully!",
        "event": event
    }
    """
