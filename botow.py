#!/usr/bin/env python3
import boto3
import logging

logging.basicConfig(level=20, format='%(asctime)s: %(name)s | LOG: %(message)s')
log = logging.getLogger(__name__)

#Takes in a tag and a value to search for and returns an dictionary of information
#about the instance: InstanceID, PriviateIP, PublicIP, InstanceState
def FindInstance(tag, value):
    log.info('Running: FindInstance', tag, value)

    ec2 = boto3.client('ec2')
    res = ec2.describe_instances(Filters=[{'Name': ('tag:'+tag),'Values': [value]}])

    try:
        instance_state = res['Reservations'][0]['Instances'][0]['State']['Name']

        try:
            instance_id = res['Reservations'][0]['Instances'][0]['InstanceId']
        except:
            instance_id = 'null'
        try:
            private_ip = res['Reservations'][0]['Instances'][0]['PrivateIpAddress']
        except:
            private_ip = 'null'
        try:
            public_ip = res['Reservations'][0]['Instances'][0]['PublicIpAddress']
        except:
            public_ip = 'null'

        instanceinfo = {
            'InstanceID': instance_id,
            'InstancePrivateIP': private_ip,
            'InstanceIP': public_ip,
            'InstanceState': instance_state
        }

    except IndexError as e:
        log.info('Cannot Find Instance')
        return False

    return instanceinfo
    

def FindSSMParam(tag, value):
    log.info('Running: FindSSMParam')

    ssm = boto3.client('ssm')
    res = ssm.describe_parameters(Filters=[{'Key': (tag),'Values': [value]}])

    try:
        ssm_info = {
            'Name': res['Parameters'][0]['Name'],
            'Value': res['Paremeters'][0][]
        }
    except IndexError as e:
        log.info('Cannot Find Parameter')
        return False

    return ssm_info
