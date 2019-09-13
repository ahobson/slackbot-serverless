# slackbot-serverless

A slackbot using the serverless framework

This bot accepts slack DMs and then sends that message back to a
channel using a webhook. The idea is that the bot might accept a
command with private information, do a thing, and then report to the
world the status of processing the thing.

## Development

    docker-compose build
    docker-compose run --rm --entrypoint npm sls install

### Running server for local development

    docker-compose up

### Deploying

Create a `docker-compose.override.yml` with your AWS credentials.
Something like:

    version: '3'
    services:
      sls:
        environment:
          - AWS_ACCESS_KEY_ID
          - AWS_SECRET_ACCESS_KEY

Or

    version: '3'
    services:
      sls:
        environment:
          - AWS_PROFILE
        volumes:
          - "~/.aws:/root/.aws"

Then do

    docker-compose run --rm sls npx sls deploy

## Slack

1. In oauth scopes, this bot will need `im:history`
1. Create a webhook (and so grant the `incoming-webhook` oauth scope.
   Copy the URL
1. In Event subscriptions, enable events and put in the URL reported
   from the serverless deployment
1. Subscribe to `message.im` workspace events
1. In Bot Users, turn on "Always Show My Bot as Online"
