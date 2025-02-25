# Vault Shield - Quantum Phantom Project

## 📌 Project Description
Vault Shield is a **high-security cloud storage solution** that encrypts, fragments, and securely stores files using **AES-256 encryption** and **Google Drive API integration**. It ensures **quantum-resistant security** with an OTP-based file retrieval system.

---

## 🚀 Features
✅ **AES-256 Encryption** – Industry-standard encryption for maximum security.  
✅ **File Fragmentation** – Splits files into multiple encrypted pieces before storage.  
✅ **Secure Google Drive API Integration** – Uses Google Drive for encrypted file storage.  
✅ **OTP Authentication for File Retrieval** – Ensures only authorized users access files.  
✅ **User-Friendly Flutter Frontend** – Seamless UI for file upload & retrieval.  
✅ **Monetization Plan** – Free 5GB, users can upgrade to premium plans for more storage.  

---

## 🛠️ Technologies Used
- **Backend:** Python (Flask), Google Drive API, AES Encryption  
- **Frontend:** Flutter (Dart), HTTP API Requests, File Picker  
- **Security:** OTP Authentication, Rate Limiting, Encrypted Metadata Storage  
- **Cloud Services:** Google Drive API, Firebase (Optional for authentication)  

---

## 📥 Installation & Setup

### 1️⃣ Backend (Flask) Setup
1. Install dependencies:
   pip install flask google-auth google-auth-oauthlib google-auth-httplib2 googleapiclient pycryptodome

2. Run the Flask backend:
   python3 app.py

### 2️⃣ Frontend (Flutter) Setup
1. Install Flutter:
   sudo snap install flutter --classic

2. Install required dependencies:
   flutter pub get

3. Run the Flutter app:
   flutter run

---

## 📌 How to Use

### 1️⃣ Upload a File
curl -X POST -F "file=@/path/to/file.txt" -F "email=user@example.com" http://127.0.0.1:5000/upload

### 2️⃣ Request OTP for File Retrieval
curl -X POST -H "Content-Type: application/json" -d '{
  "email": "user@example.com"
}' http://127.0.0.1:5000/request-otp

### 3️⃣ Retrieve the File
curl -X POST -H "Content-Type: application/json" -d '{
  "email": "user@example.com",
  "otp": "123456"
}' http://127.0.0.1:5000/retrieve

---

## 💰 Monetization Plan
- **Free Plan:** Users get **5GB storage for free**.
- **Premium Plans:** Users can **pay to expand** storage (e.g., 50GB, 100GB).
- **Enterprise Plan:** Secure cloud storage for businesses.

---

## 🔒 Security Enhancements
- **Expiring OTPs** – OTPs expire in **5 minutes**.
- **Rate Limiting on OTP Requests** – Prevents spam attacks.
- **Private Google Drive Storage** – Files are **not publicly accessible**.
- **Zero-Knowledge Encryption** – Only users have the decryption key.

---

## 🚀 Future Improvements
- **Blockchain-based Storage** – For extra security & decentralization.  
- **Quantum-Resistant Encryption** – Post-quantum cryptography methods.  
- **AI-Powered Threat Detection** – Detects suspicious file access.  

---

## 📞 Contact & Support
For questions or support, contact: **cyberlevteam@gmail.com**

---

📌 **Developed by CyberLev Team | Secure, Smart, and Future-Proof Cloud Storage 🔥**  
