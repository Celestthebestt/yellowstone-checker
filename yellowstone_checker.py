import os
import smtplib
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time


def notify(message):
    gmail_user = os.environ["EMAIL_ADDRESS"]
    gmail_password = os.environ["EMAIL_PASSWORD"]
    sent_from = gmail_user
    to = [gmail_user]
    subject = "Yellowstone Availability Update"
    body = message

    email_text = MIMEText(body)
    email_text["Subject"] = subject
    email_text["From"] = sent_from
    email_text["To"] = ", ".join(to)

    try:
        server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text.as_string())
        server.close()
        print("Email sent!")
    except Exception as e:
        print("Error sending email:", str(e))


def check_availability():
    options = Options()
    options.add_argument("--headless")  # Run without opening a browser window
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)

    url = "https://www.yellowstonenationalparklodges.com/stay/rvcamping/"  # example page
    driver.get(url)

    # wait for the calendar or booking widget to load
    time.sleep(8)

    try:
        # Example: find calendar by class name (we may adjust after seeing logs)
        calendar = driver.find_element(By.CLASS_NAME, "datepicker-calendar")
        text = calendar.text
        print("Calendar text found:\n", text)

        # Placeholder: later we’ll check for “Available” or “Sold Out”
        if "Available" in text:
            notify("Spots Available at Yellowstone! Check the site now.")
        else:
            print("No availability found.")

    except Exception as e:
        print("Error finding calendar:", str(e))

    driver.quit()


def main():
    check_availability()


if __name__ == "__main__":
    main()
