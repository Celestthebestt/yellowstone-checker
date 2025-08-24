import os
import smtplib
import requests
from bs4 import BeautifulSoup

# === CONFIG ===
URL = "https://www.yellowstonenationalparklodges.com/lodgings/campground/canyon-campground/"
TARGET_DATE = "September 13, 2025"  # The date you want to check
# ==============

def check_availability():
    try:
        response = requests.get(URL, timeout=15)
        response.raise_for_status()
    except Exception as e:
        return f"Error fetching page: {e}"

    soup = BeautifulSoup(response.text, "html.parser")

    # Simplified check: look for the target date in the page text
    if TARGET_DATE in soup.get_text():
        return f"Possible availability found for {TARGET_DATE} at Canyon Campground!"
    else:
        return None

def notify(message):
    gmail_user = os.environ["EMAIL_ADDRESS"]
    gmail_password = os.environ["EMAIL_PASSWORD"]

    sent_from = gmail_user
    to = [gmail_user]  # send notification to yourself
    subject = "Yellowstone Campground Alert"
    body = f"{message}\n\nLink: {URL}"

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
        print("✅ Email sent!")
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
