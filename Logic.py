import boto3
import ProgressPercentage
import os


s3_client = boto3.client("s3")
lambda_client = boto3.client("lambda")
s3_client.create_bucket(Bucket="uploads")

with open("FILE _NAME", "rb") as f:
    if f.name.split(".")[1] == "csv" :
        s3_client.upload_fileobj(f, "uploads", "OBJECT_NAME", Callback= ProgressPercentage('FILE_NAME'))
