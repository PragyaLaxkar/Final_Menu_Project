#!/usr/bin/python3
print("Access-Control-Allow-Origin: *")
print("Access-Control-Allow-Methods: POST, GET, OPTIONS")
print("Content-type: text/html")
print()

import boto3
import cgi

form = cgi.FieldStorage()
name = form.getvalue("name")
action = form.getvalue("action")

access_key = ''
secret_key = ''

session = boto3.Session(
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    region_name='ap-south-1'
)

iam_client = session.client('iam')

if action == "create":
    try:
        response = iam_client.create_user(UserName=name)
        print(f"IAM user '{name}' created successfully!")
    except iam_client.exceptions.EntityAlreadyExistsException:
        print(f"Error: IAM user '{name}' already exists.")
    except Exception as e:
        print(f"Error creating IAM user: {e}")

elif action == "delete":
    try:
        response = iam_client.delete_user(UserName=name)
        print(f"IAM user '{name}' deleted successfully!")
    except iam_client.exceptions.NoSuchEntityException:
        print(f"Error: IAM user '{name}' does not exist.")
    except Exception as e:
        print(f"Error deleting IAM user: {e}")

else:
    print("Invalid action specified. Please use 'create' or 'delete'.")
