import boto3
from cryptography.fernet import Fernet

bucket_name = "my-secure-bucket"
object_name = "sample.txt.enc"

s3 = boto3.client("s3")

# Download file
s3.download_file(bucket_name, object_name, "downloaded.enc")

# Decrypt
key = b"YOUR_SAVED_KEY"
cipher = Fernet(key)

with open("downloaded.enc", "rb") as f:
    encrypted_data = f.read()

decrypted_data = cipher.decrypt(encrypted_data)

with open("decrypted.txt", "wb") as f:
    f.write(decrypted_data)

print("File decrypted successfully")