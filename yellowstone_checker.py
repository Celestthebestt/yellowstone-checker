import os
import smtplib
from email.mime.text import MIMEText
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
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
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")

    driver = webdriver.Chrome(options=options)
    driver.get("https://secure.yellowstonenationalparklodges.com/booking/lodging")

    wait = WebDriverWait(driver, 20)

    try:
        # Step 1: Select campground
        where_dropdown = wait.until(
            EC.presence_of_element_located((By.ID, "campground"))
        )
        Select(where_dropdown).select_by_visible_text("Canyon Campground")

        # Step 2: Pick check-in & check-out dates (example: Sep 13 - Sep 14)
        checkin = driver.find_element(By.ID, "check-in")
        checkout = driver.find_element(By.ID, "check-out")
        checkin.clear()
        checkin.send_keys("09/13/2025")
        checkout.clear()
        checkout.send_keys("09/14/2025")

        # Step 3: Set guests
        adults = driver.find_element(By.ID, "adults")
        Select(adults).select_by_visible_text("2")

        # Step 4: Click "Check Availability"
        driver.find_element(By.ID, "availability-search-button").click()

        # Step 5: Wait for either results or popup
        time.sleep(5)

        # Look for popup
        try:
            popup = driver.find_element(By.CLASS_NAME, "modal-content")
            if "no availability" in popup.text.lower():
                print("No availability for Canyon Campground.")
            else:
                print("Popup content:", popup.text)
        except:
            # If no popup, check if results are shown
            try:
                results = driver.find_element(By.CLASS_NAME, "availability-results")
                print("Availability found!")
                notify("Spots are available at Canyon Campground! Book ASAP.")
            except:
                print("Could not determine availability status.")

    except Exception as e:
        print("Error during availability check:", str(e))

    driver.quit()


def main():
    check_availability()


if __name__ == "__main__":
    main()
