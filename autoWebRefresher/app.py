# Python Library
import os
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

# Chrome
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")  # Change this to your custom user data directory.

# Disable webdriver_manager logs
os.environ["WDM_LOG_LEVEL"] = "0"

# Initialize the Chrome driver using the Service object
driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service, options=options)

# Open the desired page(Put your own link)
driver.get('https://example.com')

# Refresh the page every 2 seconds
a=1

try:
    while True:
        time.sleep(2)
        driver.refresh()
        print(f"Page refreshed {a} times")
        a=a+1
except KeyboardInterrupt:
    print("Stopped by user.")
    driver.quit()



