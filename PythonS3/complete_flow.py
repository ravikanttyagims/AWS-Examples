import boto3

bucket_name = "py-boto3-bucket-12345-ms"

s3 = boto3.resource("s3")

# Create bucket
s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        "LocationConstraint": "us-west-2"
    }
)

# Upload file
s3.meta.client.upload_file(
    "sample.txt",
    bucket_name,
    "sample.txt"
)

# List objects
bucket = s3.Bucket(bucket_name)

for obj in bucket.objects.all():
    print(obj.key)

# Delete objects
# bucket.objects.all().delete()

# Delete bucket
# bucket.delete()

print("Workflow completed")