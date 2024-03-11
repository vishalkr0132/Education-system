import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Email configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_user = "vishalgupta.itcs@gmail.com"
smtp_password = "rumt loid kzod qubk"

def email_sending(recever, msg):
# Email content
    from_email = smtp_user
    to_email = recever
    subject = "Account Verification Message"
    # body = "This is a test email sent from a Python script using SMTP."
    html = f"""
<html>
<head>
    <style>
        body {{
            font-family: Arial, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f4f4f4;
        }}
        .container {{
            max-width: 600px;
            margin: 20px auto;
            padding: 20px;
            background-color: #ffffff;
            border-radius: 8px;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
        }}
        .header {{
            background-color: #007bff;
            color: #ffffff;
            padding: 10px;
            text-align: center;
            border-top-left-radius: 8px;
            border-top-right-radius: 8px;
        }}
        .otp {{
            font-size: 24px;
            text-align: center;
            margin: 20px 0;
            padding: 10px;
            background-color: #e9ecef;
            border-radius: 5px;
            letter-spacing: 3px;
        }}
        .footer {{
            margin-top: 20px;
            text-align: center;
            font-size: 14px;
            color: #666;
        }}
    </style>
</head>
<body>
    <div class="container">
        <div class="header">
            <h1>Welcome to Our Service</h1>
        </div>
        <p>Dear Customer,</p>
        <p>Thank you for registering with us. To complete your registration, please enter the following One Time Password (OTP) in the verification page:</p>
        <div class="otp">{msg}</div>
        <p>This OTP is valid for 10 minutes and can be used only once.</p>
        <p>If you didn't request this, please ignore this email or reach out to our support team if you have any concerns.</p>
        <div class="footer">
            <p>Best Regards,<br>Your HelpDesk Team</p>
        </div>
    </div>
</body>
</html>
"""


# Setup MIME
    message = MIMEMultipart()
    message["From"] = from_email
    message["To"] = to_email
    message["Subject"] = subject
    message.attach(MIMEText(html, "html"))

# Send email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()  # Upgrade the connection to secure
        server.login(smtp_user, smtp_password)
        text = message.as_string()
        server.sendmail(from_email, to_email, text)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()