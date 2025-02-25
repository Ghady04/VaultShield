from flask import Flask, request, jsonify
import os
import json
from werkzeug.utils import secure_filename
from Crypto.Cipher import AES
from googleapiclient.discovery import build
from google.oauth2 import service_account
from googleapiclient.http import MediaIoBaseUpload, MediaIoBaseDownload
from io import BytesIO

app = Flask(__name__)

# Configure Google Drive API credentials
SERVICE_ACCOUNT_FILE = 'hackthon-451007-742d4927157d.json'
SCOPES = ['https://www.googleapis.com/auth/drive.file']
credentials = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
drive_service = build('drive', 'v3', credentials=credentials)

# Temporary storage for OTPs
OTP_STORAGE = {}
USER_FILE_MAPPING = {}  # Store metadata file ID per email


# Helper functions
def generate_otp():
    return "".join(os.urandom(3).hex()[:6])


def encrypt_and_fragment(file_data, key, total_fragments=3):
    cipher = AES.new(key, AES.MODE_EAX)
    ciphertext, tag = cipher.encrypt_and_digest(file_data)
    fragment_size = len(ciphertext) // total_fragments + (len(ciphertext) % total_fragments > 0)
    fragments = [ciphertext[i:i + fragment_size] for i in range(0, len(ciphertext), fragment_size)]
    return fragments, cipher.nonce, tag


def upload_to_drive(fragment, filename):
    file_metadata = {'name': filename}
    media = MediaIoBaseUpload(BytesIO(fragment), mimetype='application/octet-stream')
    file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
    return file.get('id')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files or 'email' not in request.form:
        return jsonify({"error": "Missing required fields"}), 400

    file = request.files['file']
    user_email = request.form['email']
    file_path = secure_filename(file.filename)
    file.save(file_path)

    key = os.urandom(32)
    with open(file_path, 'rb') as f:
        file_data = f.read()

    fragments, nonce, tag = encrypt_and_fragment(file_data, key)
    fragment_ids = [upload_to_drive(fragment, f"{file_path}frag{i}.bin") for i, fragment in enumerate(fragments)]
    os.remove(file_path)

    metadata = {
        'fragments': fragment_ids,
        'key': key.hex(),
        'nonce': nonce.hex(),
        'tag': tag.hex()
    }

    metadata_file = BytesIO(json.dumps(metadata).encode())
    metadata_id = upload_to_drive(metadata_file.read(), f"{file_path}_metadata.json")

    # Store the metadata ID mapped to the user email
    USER_FILE_MAPPING[user_email] = metadata_id

    return jsonify({'message': 'File uploaded successfully', 'email': user_email})


@app.route('/request-otp', methods=['POST'])
def request_otp():
    data = request.json
    user_email = data['email']

    if user_email not in USER_FILE_MAPPING:
        return jsonify({"error": "No file associated with this email"}), 400

    otp = generate_otp()
    OTP_STORAGE[user_email] = otp

    return jsonify({"message": "OTP generated successfully", "otp": otp})


@app.route('/retrieve', methods=['POST'])
def retrieve_file():
    data = request.json
    entered_otp = data['otp']
    user_email = data['email']

    if user_email not in OTP_STORAGE or OTP_STORAGE[user_email] != entered_otp:
        return jsonify({"error": "Invalid or expired OTP"}), 400

    metadata_id = USER_FILE_MAPPING.get(user_email)
    if not metadata_id:
        return jsonify({"error": "No file associated with this email"}), 400

    # Retrieve metadata file from Google Drive
    metadata_request = drive_service.files().get_media(fileId=metadata_id)
    metadata_fh = BytesIO()
    downloader = MediaIoBaseDownload(metadata_fh, metadata_request)
    done = False
    while not done:
        status, done = downloader.next_chunk()
    metadata_fh.seek(0)
    metadata = json.loads(metadata_fh.read().decode())

    key = bytes.fromhex(metadata['key'])
    nonce = bytes.fromhex(metadata['nonce'])
    tag = bytes.fromhex(metadata['tag'])

    file_data = bytearray()
    for fragment_id in metadata['fragments']:
        fragment_request = drive_service.files().get_media(fileId=fragment_id)
        fragment_fh = BytesIO()
        downloader = MediaIoBaseDownload(fragment_fh, fragment_request)
        done = False
        while not done:
            status, done = downloader.next_chunk()
        fragment_fh.seek(0)
        file_data.extend(fragment_fh.read())

    cipher = AES.new(key, AES.MODE_EAX, nonce=nonce)
    try:
        decrypted_data = cipher.decrypt_and_verify(file_data, tag)
    except ValueError:
        return jsonify({"error": "Decryption failed. Data integrity compromised."}), 400

    filename = "retrieved_file"
    with open(filename, 'wb') as f:
        f.write(decrypted_data)

    del OTP_STORAGE[user_email]

    return jsonify({'message': 'File successfully retrieved and decrypted', 'file_path': filename})


if __name__ == '__main__':
    app.run(debug=True, port=5000)
