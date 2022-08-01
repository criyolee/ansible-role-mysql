#!/usr/bin/env python

import boto3 
import json 

client = boto3.client('secretsmanager')

def get_secret():
    secret_name = "ansible_vault_password"
    response = client.get_secret_value(SecretId=secret_name)
    password = json.loads(response['SecretString'])
    print(password['ansible-vault-password'])

get_secret()