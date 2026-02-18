"""To confirm that the AWS Bedrock permissions and region supports bedrock"""

import os
from dotenv import load_dotenv
import boto3

# load env
load_dotenv()

# checking bedrock client
bedrock= boto3.client('bedrock-runtime', region_name=os.getenv('AWS_REGION'))

print("Bedrock client initialized successfully!")