# Code to list IAM users
import boto3

client = boto3.client('iam', aws_access_key_id = 'AKIA4SSDS7JTD6SAWBAW', aws_secret_access_key = '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')

users_list = client.list_users()

# print(users_list['Users'])

for i in users_list['Users']:
	print(i['UserName'], i['UserId'], i['CreateDate'])

