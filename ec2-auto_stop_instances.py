# Python script to stop ec2 instances using the "instance state" name filter i.e running, terminated, etc

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
                'Values': [
                    'running',
                ],
            },
        ],
    )
    
    # Store Instance IDs in a list
    instance_id = []
    for reservation in response['Reservations']:
        for instance in reservation['Instances']:
            instance_id.append(instance['InstanceId'])

    # Stop runnning instances if they exist
    if instance:
        ec2.stop_instances(InstanceIds=instance_id)
        print(instance_id, "stopped")
    else:
        print("No running instances.")
        
    return {
        'statusCode': 200,
        'body': 'EC2 Instances stopped successfully!'
    }