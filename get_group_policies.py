import boto3

iam = boto3.client("iam")

group_name = "aws-python-automation-group"

response = iam.list_attached_group_policies(
    GroupName=group_name
)

print("Attached Policies:")

for policy in response["AttachedPolicies"]:
    print(policy["PolicyName"])