import boto3
import os
from dotenv import load_dotenv
from botocore.exceptions import NoCredentialsError

load_dotenv()

AWS_ACCESS_KEY = os.getenv("AWS_ACCESS_KEY_ID")
AWS_SECRET_KEY = os.getenv("AWS_SECRET_ACCESS_KEY")
REGION = os.getenv("AWS_REGION")
BUCKET = os.getenv("S3_BUCKET_NAME")

s3 = boto3.client('s3',
                  aws_access_key_id=AWS_ACCESS_KEY,
                  aws_secret_access_key=AWS_SECRET_KEY,
                  region_name=REGION)


def upload_image_to_s3(file_obj, filename, folder="faces"):
    """
    Uploads a file-like object to S3 under a given folder.
    Args:
        file_obj: image file (from Flask's request.files)
        filename: target filename (e.g., user123.jpg)
        folder: folder in the S3 bucket (default = "faces/")
    Returns:
        Full S3 URL of the uploaded image
    """
    key = f"{folder}/{filename}"
    try:
        s3.upload_fileobj(
            file_obj,
            BUCKET,
            key,
            ExtraArgs={
                'ContentType': file_obj.content_type,
                'ACL': 'bucket-owner-full-control'
            }
        )
        s3_url = f"https://{BUCKET}.s3.{REGION}.amazonaws.com/{key}"
        return s3_url
    except NoCredentialsError:
        print("Credentials not available")
        return None