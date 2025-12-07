import boto3

REGION = "us-east-1"

def main():
    ec2 = boto3.client("ec2", region_name=REGION)

    response = ec2.describe_instances(
        Filters=[{"Name": "instance-state-name", "Values": ["running"]}]
    )

    print("Running EC2 Instances")
    print("---------------------")

    reservations = response.get("Reservations", [])
    if not reservations:
        print("No running instances found.")
        return

    for reservation in reservations:
        for instance in reservation["Instances"]:
            instance_id = instance["InstanceId"]
            instance_type = instance["InstanceType"]
            private_ip = instance.get("PrivateIpAddress", "N/A")
            public_ip = instance.get("PublicIpAddress", "N/A")
            print(f"{instance_id} | {instance_type} | private={private_ip} | public={public_ip}")

if __name__ == "__main__":
    main()
