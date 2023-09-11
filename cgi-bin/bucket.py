#!/usr/bin/env python3
import boto3
import uuid
import cgi

aws_access_key = 'Your IAM access key'
aws_secret_key = 'Your IAM secret key'
bucket_name = f"my-bucket-{str(uuid.uuid4())[:8]}"  
region_name = 'ap-south-1'  

# Initialize the S3 client with the specified region
s3 = boto3.client('s3', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=region_name)

# Create an S3 bucket
def create_bucket():
    try:
        s3.create_bucket(Bucket=bucket_name, CreateBucketConfiguration={'LocationConstraint': region_name})
        return True, f"Bucket '{bucket_name}' created successfully."
    except Exception as e:
        return False, f"Error creating bucket: {e}"

# Print the CGI header
print("Content-type: text/html\n")

# Attempt to create the S3 bucket
success, message = create_bucket()

# Display the result
if success:
    print(f"<html><body><h1>Bucket Launched Successfully</h1></body></html>")
else:
    print(f"<html><body><h1>Error: {message}</h1></body></html>")
