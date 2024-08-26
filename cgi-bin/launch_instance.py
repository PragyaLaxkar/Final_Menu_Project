#!/usr/bin/python3
import cgi
import cgitb
import boto3
from botocore.exceptions import ClientError

cgitb.enable()

print("Content-Type: text/html\n")

form = cgi.FieldStorage()

instance_type = form.getvalue('instanceType')
image_id = form.getvalue('imageId')
region_name = form.getvalue('regionName')

def launch_aws_instance(instance_type, image_id,region_name):
    ec2 = boto3.client(
        'ec2',
        aws_access_key_id="",
        aws_secret_access_key="",
        region_name=region_name
    )
    
    try:
        response = ec2.run_instances(
            InstanceType=instance_type,
            ImageId=image_id,
            MinCount=1,
            MaxCount=1
        )
        instance_id = response['Instances'][0]['InstanceId']
        return f"Success: Instance launched with ID {instance_id}"
    except ClientError as e:
        return f"Error: {str(e)}"

if instance_type and image_id and aws_access_key and aws_secret_key and region_name:
    result = launch_aws_instance(instance_type, image_id, aws_access_key, aws_secret_key, region_name)
else:
    result = "Error: Missing one or more required fields"

print(result)
