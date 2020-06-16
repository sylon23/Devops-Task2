#EC2 Stop Script

import boto3
region = 'us-east-1'
instances = ['i-069d8b0816191303a']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.stop_instances(InstanceIds=instances)
    print('stopped your instances: ' + str(instances))



#EC2 Start Script

import boto3
region = 'us-east-1'
instances = ['i-069d8b0816191303a']
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    ec2.start_instances(InstanceIds=instances)
    print('started your instances: ' + str(instances))
