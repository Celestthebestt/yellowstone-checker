import requests
import smtplib

def check_availability():
    # 🔧 This is a placeholder until we connect to Xanterra properly.
    # For now, it always says "no availability".
    # Later, we’ll hook it up to check the real website.
    return False

def notify():
    # This just prints for now.
    # Later we’ll send you an email or text.
    print("🎉 An RV site is available at Canyon Campground on Sept 13, 2025!")

def main():
    if check_availability():
        notify()
    else:
        print("No sites yet...")

if __name__ == "__main__":
    main()
