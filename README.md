# IS 698 Final Project – Scalable AWS Cloud Architecture

## Overview

This project implements a scalable, cloud-based architecture on Amazon Web Services (AWS) as part of the IS 698 course. The solution uses multiple AWS services including VPC, EC2, RDS, S3, Lambda, and an Application Load Balancer (ALB). The infrastructure is deployed using Infrastructure as Code (IaC) with Terraform and AWS CloudFormation. Interaction with AWS is demonstrated through the AWS Management Console, AWS CLI, and Python Boto3 scripts.

---

## Architecture Components

The architecture includes:

- AWS VPC with public and private subnets across multiple Availability Zones  
- EC2 instances behind an Application Load Balancer (ALB)  
- Auto Scaling Group for scalability of the web layer  
- Amazon RDS (PostgreSQL) deployed in private subnets  
- Amazon S3 bucket (`saru-uploads`) for file storage  
- AWS Lambda function (`is698-s3-upload-logger`) for logging S3 uploads  
- Amazon CloudWatch Logs for monitoring  
- Security Groups for controlled network access  
- GitHub for version control and collaboration  

---

## Repository Structure
terraform/ # Terraform scripts for VPC, subnets, and security groups
cloudformation/ # CloudFormation template for ALB, ASG, EC2, RDS, and Lambda
python-scripts/ # Python Boto3 and EC2 metadata automation scripts
diagrams/ # AWS architecture diagram (PNG / draw.io export)
docs/ # Final project report
README.md # Project overview and setup instructions

---

## Deployment Steps

1. **Terraform – Networking**
   - Deploy VPC, public and private subnets, internet gateway, route tables, and security groups.

2. **CloudFormation – Application Stack**
   - Deploy ALB, Launch Template, Auto Scaling Group, EC2 instances, RDS PostgreSQL database, and Lambda function.

3. **Web Application**
   - EC2 instances run a simple Apache-based static web page.

4. **S3 and Lambda Integration**
   - S3 bucket `saru-uploads` triggers the Lambda function on file uploads.
   - Lambda logs upload events into CloudWatch Logs.

5. **AWS Interaction**
   - Console used for verification.
   - CLI used for managing S3, EC2 and Lambda.
   - Python Boto3 scripts used for automation.

---

## Python Automation Scripts

- `s3.py` – Creates an S3 bucket and uploads a file  
- `ec2run.py` – Lists running EC2 instances  
- `lambda.py` – Invokes the Lambda function manually  
- `ec2_metadata.py` – Retrieves EC2 metadata from inside an EC2 instance using IMDSv2  

---

## Prerequisites

- AWS Account
- Terraform
- AWS CLI
- Python 3.x
- Python libraries:
  - boto3
  - requests

---

## Course Information

This project was developed as part of the **IS 698** course to demonstrate scalable cloud architecture design, Infrastructure as Code, serverless computing and multi-interface AWS interaction.

---

## GitHub Repository

https://github.com/Sarutk-25/is698-aws-project.git

