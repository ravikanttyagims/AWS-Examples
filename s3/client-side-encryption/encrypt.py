import boto3
from cryptography.fernet import Fernet

bucket_name = "my-secure-bucket"
file_name = "sample.txt"
encrypted_file = "sample.txt.enc"

# Encryption key
key = Fernet.generate_key()
cipher = Fernet(key)

# Read file
with open(file_name, "rb") as f:
    data = f.read()

# Encrypt data
encrypted_data = cipher.encrypt(data)

# Save encrypted file
with open(encrypted_file, "wb") as f:
    f.write(encrypted_data)

print("File encrypted successfully")

# Upload to S3
s3 = boto3.client("s3")

s3.upload_file(encrypted_file, bucket_name, encrypted_file)

print("Encrypted file uploaded to S3")