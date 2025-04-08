# OTP-Validation

This Python script sends a One-Time Password (OTP) to a user's email for verification using the `smtplib` and `email` libraries. It's a basic demonstration of how email-based OTP authentication works.

---

### 🚀 Features

- Generates a random 4-digit OTP.
- Sends OTP to a specified email address using Gmail SMTP.
- Validates the OTP entered by the user.

---

### 📄 Prerequisites

Before running the script, ensure:

- You have a **Gmail account**.
- **Less secure app access** or **App Passwords** is enabled (for two-step verification accounts, use App Passwords).
- Python 3 installed with internet access.

---

### 🛠 How to Use

1. **Update your Gmail credentials in the script:**

```python
server.login("your_email@gmail.com", "your_app_password")
```

> Replace `"your_email@gmail.com"` and `"your_app_password"` with your Gmail address and app password.

2. **Run the script:**

```bash
python otp_email_sender.py
```

3. **Enter the recipient’s email address when prompted.**

4. **Check the recipient inbox for the OTP and enter it when prompted.**

---

### 🧾 Code Sample

```python
import smtplib
import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

otp = random.randint(1111,9999)
body = f"OTP for Verification is {otp}"

msg = MIMEMultipart()
msg["From"] = "your_email@gmail.com"
msg["To"] = input("Enter Email Id: ")
msg["Subject"] = "OTP For Validation"
msg.attach(MIMEText(body,'plain'))

server = smtplib.SMTP("smtp.gmail.com", 587)
server.starttls()
server.login("your_email@gmail.com", "your_app_password")
server.send_message(msg)
server.quit()

cotp = int(input("Enter OTP Received: "))
if otp == cotp:
    print("OTP Verification Success")
else:
    print("Invalid OTP")
