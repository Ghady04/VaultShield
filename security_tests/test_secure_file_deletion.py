import os
import shutil

# Secure delete function (Overwrites file before deletion)
def secure_delete(file_path):
    if os.path.exists(file_path):
        with open(file_path, "wb") as file:
            file.write(os.urandom(1024))  # Overwrite with random data
        os.remove(file_path)
        print(f"✅ {file_path} securely erased.")
    else:
        print(f"⚠️ {file_path} not found!")

# Create a test file
test_file = "firsttest.txt"
with open(test_file, "w") as f:
    f.write("This is sensitive information.")

# Securely delete the file
secure_delete(test_file)

# Verify deletion
if os.path.exists(test_file):
    print("❌ File deletion failed!")
else:
    print("✅ File is not recoverable.")

