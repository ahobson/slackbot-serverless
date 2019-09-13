# slackbot-serverless

A slackbot using the serverless framework

## Development

    docker-compose build
    docker-compose run --rm --entrypoint npm sls install

## Running server for local development

    docker-compose up

## Deploying

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
