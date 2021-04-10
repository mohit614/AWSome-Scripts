# AWSome-Scripts

Here I will include helping scripts related to AWS Cloud that makes our day to daytask easier.

- `ami-cleanup.py` is a script can be used to automatically delete AMIs that are older than X no of days.
- `ami_cleanup_ssm_doc.yaml` is SSM Automation Document that does the same task as above script, if you want to automate the deletion periodically then you can use this document.
- `sg-cleaning-port-22-3389.py` the script cleans all the SG rules in an account where port 22(ssh) and 3389(rdp) are open to the world.
