import json
import re
import boto3


client = boto3.client("ec2")
y = client.describe_security_groups()
for i in y["SecurityGroups"]:
    for j in i["IpPermissions"]:
        port = j.get("FromPort")
        if (port == 22 or port == 3389) and re.search(
            "0.0.0.0/0", str(j.get("IpRanges")), re.IGNORECASE
        ):
            print(str(i["GroupId"]) + " " + str(j["IpRanges"]))
            response = client.revoke_security_group_ingress(
                GroupId=str(i["GroupId"]),
                IpPermissions=[
                    {
                        "FromPort": port,
                        "IpProtocol": "tcp",
                        "IpRanges": [
                            {"CidrIp": "0.0.0.0/0"},
                        ],
                        "ToPort": port,
                    },
                ],
            )
        if (port == 22 or port == 3389) and re.search(
            "::/0", str(j.get("Ipv6Ranges")), re.IGNORECASE
        ):
            print(str(i["GroupId"]) + " " + str(j["Ipv6Ranges"]))
            response = client.revoke_security_group_ingress(
                GroupId=str(i["GroupId"]),
                IpPermissions=[
                    {
                        "FromPort": port,
                        "IpProtocol": "tcp",
                        "Ipv6Ranges": [
                            {"CidrIpv6": "::/0"},
                        ],
                        "ToPort": port,
                    },
                ],
            )
