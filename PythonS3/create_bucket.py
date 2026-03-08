import boto3

s3 = boto3.client("s3")

bucket_name = "py-boto3-bucket-12345-ms"

# aws configure list - use this command to check the credentials and region configuration
# aws configure get region - use this command to check the region configuration

# Create a new bucket in the specified region
# s3.create_bucket(
#     Bucket=bucket_name,
#     CreateBucketConfiguration={
#         "LocationConstraint": "us-west-2"
#     }
# )

# Enable versioning for the bucket
s3.put_bucket_versioning(
    Bucket=bucket_name,
    VersioningConfiguration={
        "Status": "Enabled"
    }
)

print("Bucket created successfully")
print("Versioning enabled")