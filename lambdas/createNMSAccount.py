import boto3
import json

def lambda_handler(event, context):
    # Create an SSM client
    ssm = boto3.client('ssm')
    
    # Retrieve the parameter
    parameter = ssm.get_parameter(
        Name='/balanceadanmsvite/authorizedEmails',  # The name of your parameter
        WithDecryption=False
    )
    
    # Extract the list of authorized emails from the parameter
    authorized_emails = parameter['Parameter']['Value'].split(',')
    
    # Extract the user's email from the event object
    user_email = event['request']['userAttributes']['email']
    
    # Check if the user's email is in the list of authorized emails
    if user_email not in authorized_emails:
        raise Exception('Email not authorized for signup')
    
    # Return the event object if the email is authorized
    return event

