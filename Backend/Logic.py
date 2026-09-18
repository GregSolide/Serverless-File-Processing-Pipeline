import boto3
import botocore
import sys
import uuid
import pandas as pd


class Logic :

    def __init__(self):
        self.s3_client = boto3.client("s3")
        
       

    def upload_file(self, file_):
        if file_ is not None:
            self.key = f"uploads/{uuid.uuid4()}-{file_.filename}"
            self.s3_client.put_object(Bucket="uploded-file",
                                Key=self.key,
                                Body=file_,
                                ServerSideEncryption='aws:kms')
            
                    
        else:
            raise Exception("You need to add a file")
    def downloading_file(self,file_):
        print(self.key)
        response= self.s3_client.get_object(Bucket='uploded-file',Key=self.key)
        print(pd.read_csv(response["Body"]))
        return 