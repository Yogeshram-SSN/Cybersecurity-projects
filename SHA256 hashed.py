#Hash pwd string using SHA-256 algorithm

import hashlib
def hash_password(password):
    password_bytes = password.encode('utf-8')
    hash_object = hashlib.sha256(password_bytes)
    password_hash = hash_object.hexdigest()
    
    return password_hash
    
password = input("Input Your Password: ")
hashed_password = hash_password(password)
print(f"Your Hashed Password is: {hashed_password}")
