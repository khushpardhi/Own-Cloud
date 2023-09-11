#!/usr/bin/env python3
import cgi
import boto3
import os

# AWS credentials and region (configure accordingly)
AWS_ACCESS_KEY_ID = 'Your IAM access key'
AWS_SECRET_ACCESS_KEY = 'Your IAM secret key'
AWS_REGION = 'ap-south-1'

# Create a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# Create an Amazon Polly client
polly = session.client('polly')

print("Content-Type: text/html\n")

print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("    <title>Text-to-Speech (Amazon Polly)</title>")
print("</head>")
print("<body>")
print("    <h1>Text-to-Speech (Amazon Polly)</h1>")

# Get user input from the form
form = cgi.FieldStorage()
text = form.getvalue("text", "")

# Synthesize speech using Amazon Polly
try:
    response = polly.synthesize_speech(
        Text=text,
        OutputFormat="mp3",
        VoiceId="Joanna"  
    )

    audio_data = response["AudioStream"].read()
    audio_file_path = "/var/www/html/output.mp3"

    with open(audio_file_path, "wb") as audio_file:
        audio_file.write(audio_data)

    print('<h2>Speech Output:</h2>')
    print('<audio controls id="audioPlayer">')
    print(f'    <source src="/output.mp3" type="audio/mpeg">')
    print('    Your browser does not support the audio element.')
    print('</audio>')

except Exception as e:
    print(f'    <p>Error: {str(e)}</p>')

print("</body>")
print("</html>")
