import json
import logging
import os

import requests

import slackbot.events.slack as slack

SIGNING_SECRET = os.getenv('SIGNING_SECRET')
WEBHOOK_URL = os.getenv('WEBHOOK_URL')

def endpoint(event, _):
    """Slack endpoint"""

    logger = logging.getLogger('handler')
    logger.setLevel(logging.INFO)
    verification_error_message = slack.verify_event(event, SIGNING_SECRET)
    if verification_error_message:
        logger.warning('Unverified message: %s', verification_error_message)
        return {
            "statusCode": 403,
            "body": json.dumps({"errorMessage": verification_error_message}),
            "headers": {"Content-type": "application/json"}
        }

    # Parse the request payload into JSON
    event_data = json.loads(event['body'])

    # Echo the URL verification challenge code back to Slack
    if "challenge" in event_data:
        logger.info('Responding to challenge')
        crdata = {"challenge": event_data.get("challenge")}
        return {
            "statusCode": 200,
            "body": json.dumps(crdata),
            "headers": {"Content-type": "application/json"}
        }

    msg = event_data["event"]["text"]

    logger.info('Posting to webhook')
    requests.post(
        WEBHOOK_URL,
        headers={'Content-type': 'application/json'},
        data=json.dumps({"text": "You said: '{}'".format(msg)})
    )

    return {
        "statusCode": 200,
        "body": json.dumps({}),
        "headers": {"Content-type": "application/json"}
    }
