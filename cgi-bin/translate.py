#!/usr/bin/env python3
import cgi
import boto3

# AWS credentials and region (configure accordingly)
AWS_ACCESS_KEY_ID = 'Your Iam access key'
AWS_SECRET_ACCESS_KEY = 'Your IAM secret access key'
AWS_REGION = 'ap-south-1'

# Create a session using your AWS credentials
session = boto3.Session(
    aws_access_key_id=AWS_ACCESS_KEY_ID,
    aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
    region_name=AWS_REGION
)

# Create an Amazon Translate client
translate = session.client('translate')

print("Content-Type: text/html\n")

print("<!DOCTYPE html>")
print("<html>")
print("<head>")
print("    <title>Text Translation (Amazon Translate)</title>")
print("</head>")
print("<body>")
print("    <h1>Text Translation (Amazon Translate)</h1>")

# Get user input from the form
form = cgi.FieldStorage()
text = form.getvalue("text", "")
source_lang = form.getvalue("sourceLang", "en")
target_lang = form.getvalue("targetLang", "fr")

# Translate the text using Amazon Translate
try:
    response = translate.translate_text(
        Text=text,
        SourceLanguageCode=source_lang,
        TargetLanguageCode=target_lang
    )

    translated_text = response["TranslatedText"]
    
    print('<h2>Translation:</h2>')
    print(f'<p id="translatedText">{translated_text}</p>')

except Exception as e:
    print(f'<p>Error: {str(e)}</p>')

print("</body>")
print("</html>")
