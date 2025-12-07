import boto3
import os
from botocore.exceptions import ClientError

# Change this to a unique bucket name
BUCKET_NAME = "saru-boto3-bucket-123"  # must be globally unique
REGION = "us-east-1"
FILE_PATH = "boto3-upload.txt"

def main():
    # Create a small file to upload
    if not os.path.exists(FILE_PATH):
        with open(FILE_PATH, "w") as f:
            f.write("Hello from Boto3 S3 upload.\n")

    s3 = boto3.client("s3", region_name=REGION)

    # Create bucket (handle us-east-1 special case)
    try:
        s3.head_bucket(Bucket=BUCKET_NAME)
        print(f"Bucket '{BUCKET_NAME}' already exists.")
    except ClientError:
        print(f"Creating bucket '{BUCKET_NAME}'...")
        if REGION == "us-east-1":
            s3.create_bucket(Bucket=BUCKET_NAME)
        else:
            s3.create_bucket(
                Bucket=BUCKET_NAME,
                CreateBucketConfiguration={"LocationConstraint": REGION},
            )
        print("Bucket created.")

    # Upload file
    key = os.path.basename(FILE_PATH)
    print(f"Uploading {FILE_PATH} to s3://{BUCKET_NAME}/{key}")
    s3.upload_file(FILE_PATH, BUCKET_NAME, key)
    print("Upload complete.")

if __name__ == "__main__":
    main()
