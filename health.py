import boto3
session = boto3.session.Session(profile_name='oblcc')
client = session.client('health')

response = client.describe_affected_entities(
    filter={
        'eventArns': [
            'string',
        ]
    },
    locale='string',
    nextToken='string',
    maxResults=10
)