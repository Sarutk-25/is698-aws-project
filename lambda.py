import boto3
import json

REGION = "us-east-1"
LAMBDA_NAME = "is698-s3-upload-logger"  # your Lambda function name

def main():
    client = boto3.client("lambda", region_name=REGION)

    payload = {}  # empty event for now

    response = client.invoke(
        FunctionName=LAMBDA_NAME,
        InvocationType="RequestResponse",
        Payload=json.dumps(payload),
    )

    status_code = response["StatusCode"]
    body = response["Payload"].read().decode("utf-8")

    print("Lambda invoke status code:", status_code)
    print("Lambda response body:")
    print(body)

if __name__ == "__main__":
    main()
