import boto3

s3 = boto3.client("s3", region_name="ap-south-1")

bucket_name = "aws-python-automation-2026-bhimashankar"

response = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        "LocationConstraint": "ap-south-1"
    }
)

print("S3 bucket created successfully!")
print("Bucket:", bucket_name)