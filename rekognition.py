import boto3
import os

rekognition = boto3.client('rekognition', region_name='us-east-1')
s3 = boto3.client('s3')

BUCKET = 'face-recognition123'  # replace with your bucket name

def find_matching_user(login_image_key):
    # List all faces stored in S3
    response = s3.list_objects_v2(Bucket=BUCKET, Prefix='faces/')
    if 'Contents' not in response:
        return None

    for obj in response['Contents']:
        stored_key = obj['Key']
        if stored_key == login_image_key or not stored_key.endswith('.jpg'):
            continue

        try:
            result = rekognition.compare_faces(
                SourceImage={'S3Object': {'Bucket': BUCKET, 'Name': stored_key}},
                TargetImage={'S3Object': {'Bucket': BUCKET, 'Name': login_image_key}},
                SimilarityThreshold=90
            )
            if result['FaceMatches']:
                matched_username = os.path.basename(stored_key).split('.')[0]
                return matched_username
        except Exception as e:
            print(f"Error comparing with {stored_key}: {e}")

    return None
