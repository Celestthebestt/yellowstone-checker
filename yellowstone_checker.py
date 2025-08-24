from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import os
import smtplib

def check_availability():
    # ✅ For testing: always “finds” availability
    return "Test: RV site available on September 13, 2025!"

def notify(message):
    gmail_user = os.environ["EMAIL_ADDRESS"]
    gmail_password = os.environ["EMAIL_PASSWORD"]

    sent_from = gmail_user
    to = [gmail_user]  # sends to yourself
    subject = "Yellowstone Campground Test Alert"
    body = f"{message}\n\nThis is a test of the Yellowstone RV checker."

    email_text = f"""\
From: {sent_from}
To: {", ".join(to)}
Subject: {subject}

{body}
"""

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(gmail_user, gmail_password)
            server.sendmail(sent_from, to, email_text)
        print("✅ Email sent successfully!")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

def main():
    message = check_availability()
    if message:
        notify(message)
    else:
        print("No availability found.")

if __name__ == "__main__":
    main()
