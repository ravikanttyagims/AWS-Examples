<!-- Create a bucket -->
aws s3 mb s3://encryption-test-bucket-ms

<!-- Create a file -->
echo "This is a test file for encryption" > testfile.txt

<!-- Upload the file to the bucket -->
aws s3 cp testfile.txt s3://encryption-test-bucket-ms/testfile.txt

<!-- Upload the file with server-side encryption -->
aws s3api put-object \
--bucket encryption-test-bucket-ms \
--key testfile.txt \
--body testfile.txt \
--server-side-encryption AES256


<!-- List KMS keys -->
aws kms list-keys

<!-- Put object with KMS encryption -->
aws s3api put-object \
--bucket encryption-test-bucket-ms \
--key testfile.txt \
--body testfile.txt \
--server-side-encryption aws:kms \
--ssekms-key-id c17327dc-4ad7-445a-b567-d9be835bb318


<!-- Put object with SSE-C -->
aws s3api put-object \
--bucket encryption-test-bucket-ms \
--key testfile.txt \
--body testfile.txt \
--server-side-encryption aws:sse-c \
--sse-customer-algorithm AES256 \
--sse-customer-key fileb://my-encryption-key.bin \
--sse-customer-key-md5 fileb://my-encryption-key.md5


<!-- Cleanup -->
aws s3 rm s3://encryption-test-bucket-ms/testfile.txt
aws s3 rb s3://encryption-test-bucket-ms
rm testfile.txt