import boto3

def list_ebs_volumes(region):

	client = boto3.client('ec2', region_name = region, aws_access_key_id = 'AKIA4SSDS7JTD6SAWBAW', aws_secret_access_key = '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')

	list_of_volumes = client.describe_volumes()

	# print(list_of_volumes['Volumes'])

	for i in list_of_volumes['Volumes']:
		print(i['VolumeId'], i['State'], i['Tags'])
		# for j in i['Tags']:
		# 	print(j)

def main():
	print ("Listing the volumes....")
	region = "ap-south-1"
	print(region)
	list_ebs_volumes(region)

main()
