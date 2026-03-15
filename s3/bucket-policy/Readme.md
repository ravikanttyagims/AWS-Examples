<!-- Create a Bucket -->
aws s3 mb s3://bucket-policy-example-ms

<!-- Set Bucket Policy -->
aws s3api put-bucket-policy \
--bucket bucket-policy-example-ms \
--policy file://policy.json

<!-- Cleanup -->
aws s3api delete-bucket-policy --bucket bucket-policy-example-ms
aws s3api delete-bucket --bucket bucket-policy-example-ms