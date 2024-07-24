import hashlib
def calculate_sha256(file_path):
    md5_hash = hashlib.sha256()
    with open(file_path, 'rb') as file:
        while chunk := file.read(65536):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()
file_path = 'File_path'
sha256_result = calculate_sha256(file_path)
print(f"SHA-256 hash of {file_path}: {sha256_result}")