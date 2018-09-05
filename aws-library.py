#!/usr/bin/env python3
import boto3
import logging

def FindInstance(tag, value):
    log.info('Running: FindInstance')

    ec2 = boto3.client('ec2')
    res = ec2.describe_instances(
    Filters=[{'Name': ('tag:'+tag),'Values': [value]}])

    try:
        iID = res['Reservations'][0]['Instances'][0]['InstanceId']
        iPIP = res['Reservations'][0]['Instances'][0]['PrivateIpAddress']
        iIP = res['Reservations'][0]['Instances'][0]['PublicIpAddress']
        iState = res['Reservations'][0]['Instances'][0]['State']['Name']

    except IndexError as e:
        log.info('Cannot Find Instance')
        return False

    instanceinfo = {
        'InstanceID': iID,
        'InstancePrivateIP': iPIP,
        'InstanceIP': iIP,
        'InstanceState': iState
    }
    
    return instanceinfo
    

def main():
    print(FindInstance("Name", "wistful"))

if __name__ == '__main__':
    #Logging Setup
    logging.basicConfig(level=logging.INFO, format='%(asctime)s: %(name)s | LOG: %(message)s')
    log = logging.getLogger(__name__)

    main()