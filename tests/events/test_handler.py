import json
import slackbot.events.handler as handler


def test_endpoint():

    event = {"headers": {}}
    r = handler.endpoint(event, {})
    assert r["body"] is not None
    rj = json.loads(r["body"])
    assert rj is not None
