import boto3
import os

s3=boto3.client('s3')

def handler(event,context):
    bucket_name=(os.environ['BUCKET_NAME'])
    key=event['Records'][0]['s3']['object']['key']
    
    try:
        print('A new file {0} has been created in bucket {1}'.format(key,bucket_name))
        return 'Success'

    except Exception as e:
        print (e)