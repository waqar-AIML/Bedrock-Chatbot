# import streamlit as st
# import requests
# import json


# # configure streamlit page
# st.set_page_config(page_title="AI Chat with Amazon bedrock",
#                    page_icon="🤖",
#                    layout="centered")

import os 
from dotenv import load_dotenv
import boto3 # For aws client
import json # for prompt


load_dotenv()

# print("Region:", os.getenv('AWS_REGION')) -- For testing 

# Create AWS Client
region = os.getenv('AWS_REGION')

bedrock = boto3.client('bedrock-runtime', region_name=region)

# print("Bedrock client created successfully: AWS connection is working.") 

# Send first prompt
prompt = "Explain GenAI in simple terms."

# Chatbot
# print("🤖 Bedrock Chatbot Started (type 'exit' to quit)\n")

# while True:
#     user_input = input("You: ")

#     if user_input.lower() == "exit":
#         break

from botocore.exceptions import ClientError

# Set the model ID, e.g., Claude 3 Haiku.
model_id = "anthropic.claude-3-haiku-20240307-v1:0"


payload = {
    "anthropic_version": "bedrock-2023-05-31",
    "max_tokens": 512,
    "temperature": 0.5,
    "messages": [
        {
            "role": "user",
            "content": [{"type": "text", "text": prompt}]
        }
    ],
    }

# Convert the payload(nartive request) to JSON.
request = json.dumps(payload)

try:
    # Invoke the model with the request.
    response = bedrock.invoke_model(modelId=model_id, body=request)

except (ClientError, Exception) as e:
    print(f"ERROR: Can't invoke '{model_id}'. Reason: {e}")
    exit(1)

# Decode the response body.
model_response = json.loads(response["body"].read())

# Extract and print the response text.
response_text = model_response["content"][0]["text"]
print(response_text)



