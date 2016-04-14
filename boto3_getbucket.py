import sys
from boto3.session import Session
import boto3

aws_key='AKIAIIEQCEZHBHAFTY4Q'
aws_secret='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'

session=Session(aws_access_key_id=aws_key,
	aws_secret_access_key=aws_secret,region_name='us-west-1')
s3=session.resource('s3')
for bucket in s3.buckets.all():
    print('bucket name:%s'%bucket.name)

bucketname=bucket.name
print(bucketname)
objkey='test.jpg'

data = open('test.jpg', 'rb')
file_obj = s3.Bucket(bucketname).put_object(Key=objkey, Body=data)

#down_url = client.generate_presigned_url(
 #   'get_object', Params={'Bucket': bucketname, 'Key': objkey},
  #  ExpiresIn= 3600000)
#print "down_rul:%s"%down_url
#bucket = s3.Bucket('predictionimage')
#for obj in bucket.objects.all():
#print(obj.key)
