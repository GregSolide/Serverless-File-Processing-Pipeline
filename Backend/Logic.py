import boto3
import Backend.ProgressPercentage as ProgressPercentage
import os


s3_client = boto3.client("s3")
lambda_client = boto3.client("lambda")
s3_client.create_bucket(Bucket="uploads")


