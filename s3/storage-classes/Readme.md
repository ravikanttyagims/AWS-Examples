<!-- Create a bucket -->
aws s3 mb s3://storage-ex-ms

<!-- Create a file -->
echo "Hello world" > hello.txt
aws s3 cp hello.txt s3://storage-ex-ms

<!-- Change Storage class -->
aws s3 cp hello.txt s3://storage-ex-ms --storage-class STANDARD_IA

<!-- Cleanup -->
aws s3 rm s3://storage-ex-ms/hello.txt
aws s3 rb s3://storage-ex-ms