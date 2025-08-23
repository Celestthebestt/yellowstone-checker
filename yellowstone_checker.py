import smtplib
import os

def check_availability():
    # 🔧 Placeholder: change to real Xanterra check later
    return True  # For testing, always triggers notification

def notify():
    gmail_user = os.environ["EMAIL_ADDRESS"]
    gmail_password = os.environ["EMAIL_PASSWORD"]
    to = gmail_user

    subject = "🎉 Yellowstone RV Site Available!"
    body = "An RV site at Canyon Campground is open for September 13, 2025!"

    email_text = f"Subject: {subject}\n\n{body}"

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.login(gmail_user, gmail_password)
        server.sendmail(gmail_user, to, email_text)
        server.close()
        print("Email sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

def main():
    if check_availability():
        notify()
    else:
        print("No sites yet...")

if __name__ == "__main__":
    main()
