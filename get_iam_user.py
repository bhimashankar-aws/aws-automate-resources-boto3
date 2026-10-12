import boto3

iam = boto3.client("iam")

username = "aws-python-automation"

response = iam.get_user(UserName=username)

user = response["User"]

print("IAM User Details:")
print("Username:", user["UserName"])
print("User ID:", user["UserId"])
print("ARN:", user["Arn"])
print("Created:", user["CreateDate"])