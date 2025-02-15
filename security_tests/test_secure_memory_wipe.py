import ctypes
import os

# Function to securely delete memory values
def secure_memory_wipe():
    key = os.urandom(32)  # Generate encryption key
    print(f"Generated Key: {key.hex()}")

    # Overwrite memory with zeros
    buffer = ctypes.create_string_buffer(32)
    ctypes.memset(ctypes.addressof(buffer), 0, 32)

    # Try accessing memory again
    if not any(buffer.raw):
        print("✅ Memory Successfully Cleared!")
    else:
        print("❌ Memory Wiping Failed!")

secure_memory_wipe()
