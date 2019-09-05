import json
import slackbot.events.handler as handler

def test_endpoint():

    r = handler.endpoint({}, {})
    assert (
        r["body"] is not None
    )
    rj = json.loads(r["body"])
    assert (
        rj["common"] == "common_thing"
    )
