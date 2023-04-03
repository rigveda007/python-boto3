import boto3
import csv

def list_s3_bucket_func(writer):

	bucket_dict = {}

	client = boto3.client('s3', aws_access_key_id = 'AKIA4SSDS7JTD6SAWBAW', aws_secret_access_key = '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')

	bucket_list = client.list_buckets()

	# print(bucket_list['Buckets'])

	for x in bucket_list['Buckets']:
		# print(x['Name'], x['CreationDate'])

		bucket_dict['Bucket_name'] = x['Name']
		bucket_dict['Bucket_creation_Date'] = x['CreationDate']

		writer.writerow(bucket_dict)

		print(bucket_dict)


def main():
	fieldnames = ['Bucket_name', 'Bucket_creation_Date']
	file_name = "D:\\sai devops\\hari-saidemy\\boto3\\segment02\\bucket_dict.csv"
	with open (file_name,"w",newline='') as csv_file:
		writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
		writer.writeheader()
		print("Printing all the buckets..")
		list_s3_bucket_func(writer)

main()
