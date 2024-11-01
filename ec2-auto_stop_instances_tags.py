# Python script to stop only running ec2 instances with a tag by using the "tag" filter

import boto3

# Define Lambda Handler Function (this serves as the entry point for the Lambda function's execution)
def lambda_handler(event, context):
  
    # Create EC2 client (this allows boto3 interact with the EC2 service in the AWS account)
    ec2 = boto3.client('ec2')

    # Retrieve all running instances
    response = ec2.describe_instances(
        Filters=[
            {
                'Name': 'instance-state-name',
                'Values': ['running'],
            },
            {
                'Name': 'tag:Env',
                'Values': ['Dev'],
            }
        ]
    )
    
    # Store Instance IDs in a list
    instance_id = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id.append(instance['InstanceId'])

    # Stop runnning instances with Env:Dev tag
    if instance:
        ec2.stop_instances(InstanceIds=instance_id)
        print(instance_id, "stopped")
    else:
        print("No running instances with Env:Dev tag.")
        
    return {
        'statusCode': 200,
        'body': 'EC2 Instances with the Env:Dev tag stopped successfully!'
        }