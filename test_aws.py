"""
->Access key valid

->Secret valid

->Region working

->IAM permissions working"""

import os
from dotenv import load_dotenv
import boto3

# load .env
load_dotenv()

# create sts client
sts = boto3.client('sts', region_name=os.getenv('AWS_REGION'))

# call AWS
identity = sts.get_caller_identity()
print("✅ AWS access is working")
print(identity)


