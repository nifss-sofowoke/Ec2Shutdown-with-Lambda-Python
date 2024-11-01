# Python script to stop ec2 instances using boto3 

import boto3

# Create EC2 client (this allows boto3 interact with the EC2 service in the AWS account)
ec2 = boto3.client('ec2')

# Specify instances to stop using their instance Id
instance_id = 'string'

# Create a stop instance function using the instanceId and response syntax from the documentation
def stop_instance(client, instance_id):
    response = ec2.stop_instances(InstanceIds=[instance_id])
    print(instance_id, 'stopped')
    
# Added a conditional if statement to define the code that it should only run when executed directly by Python
if __name__ == '__main__':
    # invoke the stop_instance function
    stop_instance(ec2, instance_id)