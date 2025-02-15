import os
import time

# Generate a one-time encryption key
def generate_temporary_key():
    key = os.urandom(32)  # 256-bit AES key
    print(f"Generated Key: {key.hex()}")
    return key

# Self-destruct key after a delay
def self_destruct_key(key, delay=3):
    print(f"Key will self-destruct in {delay} seconds...")
    time.sleep(delay)
    del key  # Destroy the key
    try:
        print(f"Trying to access key: {key}")
    except NameError:
        print("✅ Key Successfully Destroyed!")

# Run the test
key = generate_temporary_key()
self_destruct_key(key)
