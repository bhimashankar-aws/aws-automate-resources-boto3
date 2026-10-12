import boto3

s3 = boto3.client("s3", region_name="ap-south-1")

bucket_name = "aws-python-automation-2026-bhimashankar"
file_name = "test.txt"

s3.download_file(bucket_name, file_name, "downloaded_test.txt")

print("File downloaded successfully!")