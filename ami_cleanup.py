#!/usr/bin/python3

import boto3
from dateutil.parser import parse
import datetime

age = 0

def days_old(date):
    get_date_obj = parse(date)
    date_obj = get_date_obj.replace(tzinfo=None)
    diff = datetime.datetime.now() - date_obj
    return diff.days

ec2 = boto3.client('ec2')
sts_client = boto3.client('sts')
response = sts_client.get_caller_identity()

print("\n\nScript running------------------>")
print("The script is using following role permissions: " + str(response['Arn']));


amis = ec2.describe_images(Owners=['self'])


for ami in amis['Images']:
    create_date = ami['CreationDate']
    ami_id = ami['ImageId']
    day_old = days_old(create_date)
    
    if day_old > age:
        print("Deleting below AMIs: \n")
        print( "AMI-ID: " + ami['ImageId'] + "\t\tCreation Date: "+ ami['CreationDate']+"\t\tDays old:"+ str(day_old) )
        ec2.deregister_image(ImageId=ami_id)
