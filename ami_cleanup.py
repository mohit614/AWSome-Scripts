#!/usr/bin/python3

import boto3
from dateutil.parser import parse
import datetime
import re

age = 0 #Default it is 7 days #you can change it

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
    ami_id = ami['ImageId']
    create_date = ami['CreationDate']
    snapshot_id = ami['BlockDeviceMappings'][0]['Ebs']['SnapshotId']

    day_old = days_old(create_date)
    # print( "AMI-ID: " + ami['ImageId'] + "\t\tCreation Date: "+ ami['CreationDate']+"\t\tDays old:"+ str(day_old) )
    if day_old >= age:
        print("Deleting below AMIs with corresponding snapshot : \n")
        print( "AMI-ID: " + ami['ImageId'] + "\t\tCreation Date: "+ ami['CreationDate']+"\t\tDays old:"+ str(day_old) + "Snapshot : " + snapshot_id)
        ec2.deregister_image(ImageId=ami_id)
        ec2.delete_snapshot(SnapshotId=snapshot_id) #deleting snapshot
