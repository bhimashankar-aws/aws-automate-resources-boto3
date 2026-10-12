import boto3

ec2 = boto3.client("ec2", region_name="ap-south-1")

instance_id = "i-0e3389a7ef664dac2"

response = ec2.stop_instances(
    InstanceIds=[instance_id]
)

print("EC2 stop command sent successfully!")
print("Instance ID:", instance_id)