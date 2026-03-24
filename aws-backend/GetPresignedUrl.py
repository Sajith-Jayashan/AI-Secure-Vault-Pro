import boto3
import json
import os

# Initialize S3 client
s3 = boto3.client('s3')

# PLACEHOLDERS: These should be set as Environment Variables in the Lambda Console
BUCKET_NAME = os.environ.get('UPLOAD_BUCKET', 'YOUR_IMAGE_BUCKET_NAME')

def lambda_handler(event, context):
    try:
        # Parse request body
        body = json.loads(event['body'])
        file_name = body['fileName']
        file_type = body['fileType']

        # Generate the Presigned URL (Valid for 5 minutes)
        presigned_url = s3.generate_presigned_url(
            'put_object',
            Params={
                'Bucket': BUCKET_NAME,
                'Key': file_name,
                'ContentType': file_type
            },
            ExpiresIn=300
        )

        return {
            'statusCode': 200,
            'headers': {
                "Access-Control-Allow-Origin": "*",
                "Access-Control-Allow-Headers": "Content-Type",
                "Access-Control-Allow-Methods": "OPTIONS,POST"
            },
            'body': json.dumps({'uploadUrl': presigned_url})
        }
    except Exception as e:
        print(f"Error: {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps({'error': 'Failed to generate upload URL'})
        }