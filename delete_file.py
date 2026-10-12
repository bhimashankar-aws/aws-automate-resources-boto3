import boto3

s3 = boto3.client("s3", region_name="ap-south-1")

bucket_name = "aws-python-automation-2026-bhimashankar"
file_name = "test.txt"

s3.delete_object(
    Bucket=bucket_name,
    Key=file_name
)

print("File deleted successfully!")