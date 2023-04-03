import boto3

def list_roles(access_key):

	client = boto3.client('iam', aws_access_key_id = access_key, aws_secret_access_key = '1e4o9RxcJBqtxrZbHtZboFTs8omP/siZmaxmZCYs')

	role_list = client.list_roles()

	# print(role_list['Roles'])

	for i in role_list['Roles']:
		print(i['RoleName'], i['RoleId'], i['CreateDate'])

def main():
	print("Listing all the rules")
	access_key = "AKIA4SSDS7JTD6SAWBAW"
	print(access_key)
	list_roles(access_key)

main()
