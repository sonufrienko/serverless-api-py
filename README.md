# Serverless Rest API with Python on AWS

## Features

- Python
- Serverless Framework
- AWS ApiGateway (HTTP API)
- AWS Lambda
- AWS DynamoDB

## Getting Started

Deploy

```
sls plugin install -n serverless-python-requirements
sls deploy
```

## How to use

List devices

```
http <api_url>/devices
```

Add device

```
http POST <api_url>/devices name="raspberypi"
```

Remove device

```
http DELETE <api_url>/devices/<device_id>
```
