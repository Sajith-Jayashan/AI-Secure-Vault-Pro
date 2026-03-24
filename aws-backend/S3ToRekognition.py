import boto3
import json
import os
from datetime import datetime

# Initialize AWS clients
rekognition = boto3.client('rekognition')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get('DYNAMODB_TABLE', 'FileMetadata'))

def lambda_handler(event, context):
    # Get bucket and key from the S3 event
    bucket = event['Records'][0]['s3']['bucket']['name']
    key = event['Records'][0]['s3']['object']['key']

    try:
        # 1. Detect Labels using Rekognition
        response = rekognition.detect_labels(
            Image={'S3Object': {'Bucket': bucket, 'Name': key}},
            MaxLabels=5,
            MinConfidence=75
        )

        labels = [label['Name'] for label in response['Labels']]
        timestamp = datetime.now().isoformat()

        # 2. Store metadata in DynamoDB
        table.put_item(
            Item={
                'FileID': key,        # Primary Key (Matches your screenshot)
                'Labels': labels,     # AI Generated tags
                'Timestamp': timestamp,
                'Bucket': bucket
            }
        )
        
        return {'statusCode': 200, 'body': json.dumps('AI Tagging Successful')}

    except Exception as e:
        print(f"Error processing {key}: {str(e)}")
        raise e