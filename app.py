import streamlit as st
import boto3
import pandas as pd

# Initialize the S3 client
s3_client = boto3.client('s3', aws_access_key_id='YOUR_AWS_ACCESS_KEY', 
                         aws_secret_access_key='YOUR_AWS_SECRET_KEY', 
                         region_name='YOUR_AWS_REGION')

def list_files_in_bucket(bucket_name):
    response = s3_client.list_objects_v2(Bucket=bucket_name)
    if 'Contents' in response:
        return [file['Key'] for file in response['Contents']]
    return []

def fetch_file_from_s3(bucket_name, file_key):
    obj = s3_client.get_object(Bucket=bucket_name, Key=file_key)
    data = obj['Body'].read().decode('utf-8')
    return data

# Streamlit App
st.title("Sensory Verse")
st.write("Welcome to Sensory Verse, a platform to assist blind and deaf children with their studies.")

bucket_name = st.text_input("Enter the S3 Bucket Name:", "your-bucket-name")

if bucket_name:
    files = list_files_in_bucket(bucket_name)
    selected_file = st.selectbox("Select a file to display:", files)

    if selected_file:
        file_content = fetch_file_from_s3(bucket_name, selected_file)
        st.text_area("File Content", file_content, height=300)

# Additional content and features for your web app can be added here

