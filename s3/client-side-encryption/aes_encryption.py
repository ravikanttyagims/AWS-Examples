from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import boto3

key = get_random_bytes(32)
cipher = AES.new(key, AES.MODE_EAX)

with open("sample.txt", "rb") as f:
    data = f.read()

ciphertext, tag = cipher.encrypt_and_digest(data)

with open("encrypted.bin", "wb") as f:
    f.write(cipher.nonce + tag + ciphertext)

s3 = boto3.client("s3")

s3.upload_file("encrypted.bin", "my-secure-bucket", "encrypted.bin")