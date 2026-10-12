import boto3

iam = boto3.client("iam")

username = "aws-python-automation"

response = iam.list_groups_for_user(
    UserName=username
)

print("Groups for IAM User:")

for group in response["Groups"]:
    print(group["GroupName"])