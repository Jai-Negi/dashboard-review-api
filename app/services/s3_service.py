# app/services/s3_service.py

import boto3
from botocore.exceptions import BotoCoreError, ClientError
import json

class S3Service:
    def __init__(self, aws_access_key, aws_secret_key, bucket_name, region_name='us-east-1'):
        self.bucket_name = bucket_name
        self.s3_client = boto3.client(
            's3',
            region_name= region_name,
            aws_access_key_id=aws_access_key,
            aws_secret_access_key=aws_secret_key,
        )
    
    def upload_json(self, key: str, data: dict):
        """
        Uploads a dictionary as a JSON file to S3 with the given key.
        """
        json_content = json.dumps(data)
        try:
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=key,
                Body=json_content,
                ContentType='application/json'
            )
        except (BotoCoreError, ClientError) as e:
            raise Exception(f"Failed to upload JSON to S3: {e}")

    def upload_file(self, key: str, file_obj):
        """
        Uploads a file-like object to S3 with the given key.
        """
        try:
            self.s3_client.upload_fileobj(
                Fileobj=file_obj,
                Bucket=self.bucket_name,
                Key=key
            )
        except (BotoCoreError, ClientError) as e:
            raise Exception(f"Failed to upload file to S3: {e}")
