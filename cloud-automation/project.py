import boto3
from datetime import date, datetime, timedelta,timezone
from datetime import date
import csv
import os
from botocore.exceptions import ClientError
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

def access_key_age(writer):

	csv_dict = {}

	client = boto3.client('iam', aws_access_key_id = 'AKIA4SSDS7JTD6SAWBAW', aws_secret_access_key = '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')

	list_iam_users = client.list_users()
	# print(list_iam_users['Users'])
	for i in list_iam_users['Users']:
		iam_username = i['UserName']
		# print(iam_username)
		access_key_response = client.list_access_keys(UserName = iam_username)
		# print(access_key_response['AccessKeyMetadata'])
		for j in access_key_response['AccessKeyMetadata']:
			# print(j['UserName'], j['AccessKeyId'], j['CreateDate'])

			todays_date = datetime.now(timezone.utc)
			access_key_life = (todays_date - j['CreateDate']).days 

			# print(j['UserName'], access_key_life)

			if (access_key_life >= 50):
				# print(j['UserName'], access_key_life)
				csv_dict['IAM_Username'] = j['UserName']
				csv_dict['AccesKey'] = j['AccessKeyId']
				csv_dict['Age'] = access_key_life

				writer.writerow(csv_dict)
				print(csv_dict)

def send_email_report(file_name):
	SENDER = "neelbanerjee.ciem@gmail.com"
	RECIPIENT = "neelbanerjee.ciem@gmail.com"
	SUBJECT = "Accesskey 30 Age Data"
	ATTACHMENT = file_name
	BODY_HTML = """\
	<html>
	<head></head>
	<body>
	<h3>Hi All</h3>
	<p>Please see the attached file for a list of Accesskey those are created more than 50 days ago.</p>
	</body>
	</html>
	"""
	CHARSET = "utf-8"
	client = boto3.client('ses')
	msg = MIMEMultipart('mixed')
	msg['Subject'] = SUBJECT 
	msg['From'] = SENDER 
	msg['To'] = RECIPIENT
	
	msg_body = MIMEMultipart('alternative')
	htmlpart = MIMEText(BODY_HTML.encode(CHARSET), 'html', CHARSET)
	msg_body.attach(htmlpart)
	att = MIMEApplication(open(ATTACHMENT, 'rb').read())
	att.add_header('Content-Disposition','attachment',filename=os.path.basename(ATTACHMENT))
	msg.attach(msg_body)
	msg.attach(att)
	try:
	    response = client.send_raw_email(
	        Source=SENDER,
	        Destinations=[
	            RECIPIENT
	        ],
	        RawMessage={
	            'Data':msg.as_string(),
	        }
	    ) 
	except ClientError as e:
	    print(e.response['Error']['Message'])
	else:
	    print("Email sent! Message ID:"),
	    print(response['MessageId'])

def lambda_handler(event, context):
	fieldnames = ['IAM_Username', 'AccesKey', 'Age' ]
	file_name = "D:\\sai devops\\hari-saidemy\\boto3\\segment02\\csv_dict.csv"
	with open (file_name,"w",newline='') as csv_file:
		writer = csv.DictWriter(csv_file,fieldnames=fieldnames)
		writer.writeheader()
		# print("Printing the access key age of every user")
		access_key_age(writer)
	send_email_report(file_name)


main()
