import boto3

s3 = boto3.client("s3", region_name="ap-south-1")

bucket_name = "aws-python-automation-2026-bhimashankar"
file_name = "test.txt"

with open(file_name, "w") as file:
    file.write("Hello from AWS Python Automation!")

s3.upload_file(file_name, bucket_name, file_name)

print("File uploaded successfully!")