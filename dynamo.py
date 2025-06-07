import boto3
s3 = boto3.client('s3')
s3.head_object(Bucket='face-recognition123', Key='faces/bunny.jpg')
