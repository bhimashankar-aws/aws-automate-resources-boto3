import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

ami_id = "ami-0a59fb4395466ed05"

response = ec2.run_instances(
    ImageId=ami_id,
    InstanceType="t3.micro",
    MinCount=1,
    MaxCount=1
)

instance_id = response["Instances"][0]["InstanceId"]

print("EC2 instance launched successfully!")
print("Instance ID:", instance_id)