#!/usr/bin/env python3
import boto3
import cgi

# Set the content-type header
print("Content-type: text/html\n")

# AWS IAM credentials (if not using IAM roles)
aws_access_key = 'Your IAM access key'
aws_secret_key = 'Your IAM secret key'
region_name = 'ap-south-1'  

# Initialize the EC2 client
ec2 = boto3.client('ec2', aws_access_key_id=aws_access_key, aws_secret_access_key=aws_secret_key, region_name=region_name)

# EC2 instance configuration
image_id = 'ami-0ded8326293d3201b'
instance_type = 't2.micro'  

# Launch the EC2 instance
try:
    response = ec2.run_instances(
        ImageId=image_id,
        InstanceType=instance_type,
        MinCount=1,
        MaxCount=1
    )

    instance_id = response['Instances'][0]['InstanceId']
    print("<html><head><title>EC2 Instance Launched</title></head><body>")
    print("<h1>EC2 Instance Launched Successfully</h1>")
    print(f"<p>Instance ID: {instance_id}</p>")
    print("<a href='launch_ec2.html'>Go back</a>")
    print("</body></html>")
except Exception as e:
    print("<html><head><title>Error</title></head><body>")
    print("<h1>Error launching EC2 instance</h1>")
    print(f"<p>{e}</p>")
    print("<a href='launch_ec2.html'>Go back</a>")
    print("</body></html>")
