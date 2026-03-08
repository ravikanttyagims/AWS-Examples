import boto3

s3 = boto3.resource("s3")

bucket = s3.Bucket("py-boto3-bucket-12345-ms")

bucket.objects.all().delete()

bucket.delete()

print("Bucket deleted")