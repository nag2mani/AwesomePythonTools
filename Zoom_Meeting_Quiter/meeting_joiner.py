from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
import time
import pyautogui

# Path to Chrome and ChromeDriver
chrome_path = "C:/Program Files/Google/Chrome/Application/chrome.exe"
chromedriver_path = "C:/path/to/chromedriver.exe"  # Update with actual path

# Set up Chrome options
chrome_options = Options()
chrome_options.binary_location = chrome_path
chrome_options.add_argument(f"--user-data-dir=C:/Users/YourUsername/AppData/Local/Google/Chrome/User Data")
chrome_options.add_argument("--profile-directory=Profile 2")  # Change this based on your profile

# Start WebDriver
service = Service(chromedriver_path)
driver = webdriver.Chrome(service=service, options=chrome_options)

# Open Google Calendar
driver.get("https://calendar.google.com")

time.sleep(5)  # Wait for the calendar to load

# Find the 4 PM event
events = driver.find_elements(By.CSS_SELECTOR, "[role='button']")  # Adjust selector if needed

zoom_link = None
for event in events:
    if "4:00 PM" in event.text:
        event.click()
        time.sleep(2)
        links = driver.find_elements(By.TAG_NAME, "a")
        for link in links:
            if "zoom.us" in link.get_attribute("href"):
                zoom_link = link.get_attribute("href")
                break
        break

# If a Zoom link is found, open it
if zoom_link:
    driver.get(zoom_link)
    time.sleep(5)

    # Auto join if required
    pyautogui.press("enter")  # Press enter to join the meeting

    print("Joined the Zoom meeting!")
else:
    print("No Zoom link found in the 4 PM event.")

driver.quit()
