#!/usr/bin/env python3
import boto3
import logging

logging.basicConfig(level=20, format='%(asctime)s: %(name)s | LOG: %(message)s')
log = logging.getLogger(__name__)

#Takes in a tag and a value to search for and returns an dictionary of information
#about the instance: InstanceID, PriviateIP, PublicIP, InstanceState
def FindInstance(tag, value):
    log.info('Running: FindInstance')

    ec2 = boto3.client('ec2')
    res = ec2.describe_instances(Filters=[{'Name': ('tag:'+tag),'Values': [value]}])

    try:
        instanceinfo = {
            'InstanceID': res['Reservations'][0]['Instances'][0]['InstanceId'],
            'InstancePrivateIP': res['Reservations'][0]['Instances'][0]['PrivateIpAddress'],
            'InstanceIP': res['Reservations'][0]['Instances'][0]['PublicIpAddress'],
            'InstanceState': res['Reservations'][0]['Instances'][0]['State']['Name']
        }

    except IndexError as e:
        log.info('Cannot Find Instance')
        return False

    return instanceinfo
    

def FindSSMParam(tag, value):
    log.info('Running: FindSSMParam')

    ssm = boto3.client('ssm')
    res = ssm.describe_parameters(Filters=[{'Name': ('tag:'+tag)}])
    return True