<!-- Create a Bucket -->
aws s3 mb s3://cors-ex-ms

<!-- Change block public access -->
aws s3api put-public-access-block \
--bucket cors-ex-ms \
--public-access-block-configuration "BlockPublicAcls=true,IgnorePublicAcls=true,BlockPublicPolicy=false,RestrictPublicBuckets=false"

<!-- Create a bucket policy -->
aws s3api put-bucket-policy \
--bucket cors-ex-ms \
--policy file://policy.json


<!-- Turn on Static Website Hosting -->
aws s3api put-bucket-website \
--bucket cors-ex-ms \
--website-configuration file://website.json


<!-- Upload index.html and include a resource that would be cross-origin -->
aws s3 cp index.html s3://cors-ex-ms/index.html

<!-- View the website and see if index.html is there -->
http://cors-ex-ms.s3-website-us-west-2.amazonaws.com/index.html

<!-- Get the website endpoint -->
aws s3api get-bucket-website \
--bucket cors-ex-ms \
--query "WebsiteConfiguration.[Endpoint]" \
--output text

<!-- Set CORS on our bucket -->
aws s3api put-bucket-cors \
--bucket cors-ex-ms \
--cors-configuration file://cors.json


<!-- Cleanup -->
aws s3 rm s3://cors-ex-ms/index.html
aws s3api delete-bucket-cors \
--bucket cors-ex-ms