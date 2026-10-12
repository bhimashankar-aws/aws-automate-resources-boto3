# AWS Resource Automation Using Python & Boto3

## Objective

This project automates common AWS resource management tasks using Python and the AWS SDK for Python (Boto3).

The project demonstrates how Python can be used to interact with AWS services programmatically instead of performing every operation manually through the AWS Management Console.

The automation covers three major AWS services:

- Amazon S3
- Amazon EC2
- AWS IAM

The project includes operations such as creating and managing S3 resources, launching and managing EC2 instances, and retrieving IAM user, group, and policy information.

---

## AWS Services Used

- **Amazon S3** – Create buckets, list buckets, upload files, download files, and delete objects.
- **Amazon EC2** – Launch, stop, and terminate EC2 instances.
- **AWS IAM** – List IAM users, retrieve user details, view user groups, and retrieve attached group policies.
- **AWS STS** – Verify the authenticated AWS identity.
- **Boto3** – Python SDK used to interact with AWS services programmatically.

---

## Architecture / Workflow

The project follows a Python-based AWS automation workflow:

```text
                    Python Scripts
                          |
                          v
                     Boto3 SDK
                          |
                          v
                    AWS Services
                   /     |     \
                  /      |      \
                S3      EC2      IAM
                |        |        |
             Buckets   Instances  Users
             Objects             Groups
                                 Policies
Workflow
Python scripts are executed from the local development environment.
Boto3 connects the Python application with AWS services.
AWS credentials authenticate the requests.
The Python scripts send API requests to AWS.
Amazon S3 operations manage buckets and objects.
Amazon EC2 operations manage EC2 instances.
AWS IAM operations retrieve users, groups, and policies.
AWS STS verifies the authenticated AWS identity.
Project Structure
aws-resource-automation/
│
├── create_s3_bucket.py
├── list_buckets.py
├── upload_file.py
├── download_file.py
├── delete_file.py
│
├── launch_ec2.py
├── stop_ec2.py
├── terminate_ec2.py
│
├── list_iam_users.py
├── get_iam_user.py
├── get_iam_groups.py
├── get_group_policies.py
│
├── test.txt
├── downloaded_test.txt
└── README.md
S3 Automation
create_s3_bucket.py – Creates an S3 bucket.
list_buckets.py – Lists available S3 buckets.
upload_file.py – Uploads a file to S3.
download_file.py – Downloads an S3 object.
delete_file.py – Deletes an S3 object.
EC2 Automation
launch_ec2.py – Launches a new EC2 instance.
stop_ec2.py – Stops an EC2 instance.
terminate_ec2.py – Terminates an EC2 instance.
IAM Automation
list_iam_users.py – Lists IAM users.
get_iam_user.py – Retrieves IAM user details.
get_iam_groups.py – Retrieves groups associated with an IAM user.
get_group_policies.py – Lists policies attached to an IAM group.
Implementation and Testing
1. S3 Automation

The S3 automation was tested successfully using Python scripts with Boto3.

Operations performed:

Created an S3 bucket.
Listed S3 buckets.
Uploaded test.txt.
Downloaded the file as downloaded_test.txt.
Verified the downloaded file content.
Deleted the uploaded object.
2. EC2 Automation

The EC2 automation was tested successfully.

Operations performed:

Launched a t3.micro EC2 instance.
Verified the instance state as running.
Stopped the instance using Python.
Verified the instance state as stopped.
Terminated the instance using Python.
Verified the instance state as terminated.
3. IAM Automation

The IAM automation was tested successfully.

Operations performed:

Listed IAM users.
Retrieved IAM user details.
Retrieved groups associated with the IAM user.
Retrieved policies attached to the IAM group.

The IAM group was configured with the required permissions for the project operations.

4. AWS Identity Verification

AWS STS was used to verify the authenticated AWS identity.

Command:

aws sts get-caller-identity

The command successfully verified the AWS identity used by the AWS CLI environment.

How to Run
Prerequisites
Python 3.x
AWS Account
AWS CLI
Boto3
Configured AWS credentials
Install Boto3
pip install boto3
Configure AWS CLI
aws configure

Enter the required AWS credentials and select the appropriate AWS region.

Verify AWS Identity
aws sts get-caller-identity
Run S3 Scripts
python create_s3_bucket.py
python list_buckets.py
python upload_file.py
python download_file.py
python delete_file.py
Run EC2 Scripts
python launch_ec2.py
python stop_ec2.py
python terminate_ec2.py
Run IAM Scripts
python list_iam_users.py
python get_iam_user.py
python get_iam_groups.py
python get_group_policies.py
Security Practices
AWS credentials should not be stored inside Python source code.
AWS credentials should not be committed to GitHub.
IAM permissions should follow the principle of least privilege.
Sensitive information such as AWS account numbers, access keys, secret keys, and ARNs should not be published in the public repository.
AWS resources should be stopped or terminated when they are no longer required to avoid unnecessary charges.
Key Learnings

Through this project, I learned:

How to use Python with Boto3.
How to automate AWS services programmatically.
How to perform S3 operations using Python.
How to launch and manage EC2 instances using Python.
How to retrieve IAM users, groups, and policies.
How AWS CLI and STS can be used to verify AWS identity.
How AWS permissions affect programmatic resource management.
How automation can reduce repetitive manual tasks in AWS.
Project Outcome

This project successfully demonstrates how Python and Boto3 can be used to automate common AWS resource management tasks.

Instead of performing every operation manually through the AWS Management Console, the project uses Python scripts to interact with AWS services through APIs.

The project provides practical experience with AWS automation, cloud resource management, IAM permissions, and Python-based DevOps workflows.

## Screenshots

### Project Screenshot 1
![AWS Resource Automation Screenshot 1](Screenshot%202026-10-12%20160814.png)

### Project Screenshot 2
![AWS Resource Automation Screenshot 2](Screenshot%202026-10-12%20160856.png)

### Project Screenshot 3
![AWS Resource Automation Screenshot 3](Screenshot%202026-10-12%20160911.png)

### Project Screenshot 4
![AWS Resource Automation Screenshot 4](Screenshot%202026-10-12%20160929.png)

### Project Screenshot 5
![AWS Resource Automation Screenshot 5](Screenshot%202026-10-12%20160946.png)


S3 bucket creation and file operations
EC2 instance launch, stop, and termination
IAM user and group information
IAM group policies
Successful Python script execution
AWS identity verification using STS
Author

Bhimashankar Dhumal

AWS Cloud & Python Automation Learner
