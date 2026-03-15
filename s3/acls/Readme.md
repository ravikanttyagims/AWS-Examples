<!-- Create a bucket -->
aws s3api create-bucket --bucket acls-ex-ms --region us-east-1

<!-- Turn off Block Public Access for ACLs -->
aws s3api put-public-access-block \
--bucket acls-ex-ms \
--public-access-block-configuration "BlockPublicAcls=false,IgnorePublicAcls=false,BlockPublicPolicy=true,RestrictPublicBuckets=true"

aws s3api get-public-access-block \
--bucket acls-ex-ms


<!-- Change Bucket Ownership -->
aws s3api put-bucket-ownership-controls \
--bucket acls-ex-ms \
--ownership-controls "Rules=[{ObjectOwnership=BucketOwnerPreferred}]"