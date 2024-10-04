import hashlib

def hash_password(password):

    sha256_hash = hashlib.sha256(password.encode()).hexdigest()
    return sha256_hash

password = input("Enter a password: ")

hashed_password = hash_password(password)
print(f"SHA-256 hash: {hashed_password}")
