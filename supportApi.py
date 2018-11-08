import boto3
session = boto3.session.Session(profile_name='oblcc')

client = session.client('support', region_name='us-east-1')
response = client.describe_services(
    serviceCodeList=[
        'string',
    ],
    language='string'
)