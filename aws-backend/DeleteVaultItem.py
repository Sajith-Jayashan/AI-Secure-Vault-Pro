import boto3
import json
import os

s3 = boto3.client('s3')
dynamodb = boto3.resource('dynamodb')
table = dynamodb.Table(os.environ.get('DYNAMODB_TABLE', 'FileMetadata'))

def lambda_handler(event, context):
    try:
        body = json.loads(event['body'])
        file_id = body['FileID']
        bucket = os.environ.get('UPLOAD_BUCKET', 'YOUR_IMAGE_BUCKET_NAME')

        # 1. Delete from S3
        s3.delete_object(Bucket=bucket, Key=file_id)

        # 2. Delete from DynamoDB
        table.delete_item(Key={'FileID': file_id})

        return {
            'statusCode': 200,
            'headers': { "Access-Control-Allow-Origin": "*" },
            'body': json.dumps("Record and file deleted successfully")
        }
    except Exception as e:
        print(f"Delete error: {str(e)}")
        return {'statusCode': 500, 'body': json.dumps("Failed to delete")}