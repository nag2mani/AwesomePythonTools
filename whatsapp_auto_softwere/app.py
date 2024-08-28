# Python Library
import os
from time import sleep
from selenium import webdriver
from urllib.parse import quote
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


# Chrome
options = Options()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument("--profile-directory=Default")
options.add_argument("--user-data-dir=/var/tmp/chrome_user_data")  # Change this to your custom user data directory


# Disable webdriver_manager logs
os.environ["WDM_LOG_LEVEL"] = "0"


# Define colors for console output
class style():
    BLACK = '\033[30m'
    RED = '\033[31m'
    GREEN = '\033[32m'
    YELLOW = '\033[33m'
    BLUE = '\033[34m'
    MAGENTA = '\033[35m'
    CYAN = '\033[36m'
    WHITE = '\033[37m'
    UNDERLINE = '\033[4m'
    RESET = '\033[0m'


# Introduction banner
print(style.BLUE)
print("**********************************************************")
print("*****      This tool is maintained by Nagmani Kumar     **")
print("**********************************************************")
print(style.RESET)


# Read the message from file
with open("message.txt", "r", encoding="utf8") as f:
    message = f.read()


print(style.YELLOW + '\nThis is your message-')
print(style.GREEN + message)
print("\n" + style.RESET)


# URL encode the message.
message = quote(message)


# Read the numbers from file
with open("numbers.txt", "r") as f:
    numbers = [line.strip() for line in f if line.strip() != ""]
total_number = len(numbers)
print(style.RED + 'We found ' + str(total_number) + ' numbers in the file' + style.RESET)


# Time to wait before sending the message
delay = 20


# Time to wait between messages
wait_time_between_messages = 4


# Initialize the Chrome driver using the Service object
driver_service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=driver_service, options=options)
print('Once your browser opens up sign in to WhatsApp Web')
driver.get('https://web.whatsapp.com')


# Wait for user to log in to WhatsApp Web
input(style.MAGENTA + "AFTER logging into WhatsApp Web is complete and your chats are visible, press ENTER..." + style.RESET)


# Loop through the numbers and send the message
for idx, number in enumerate(numbers):
    number = number.strip()
    if not number:
        continue
    print(style.YELLOW + '{}/{} => Sending message to {}.'.format((idx + 1), total_number, number) + style.RESET)
    try:
        url = f'https://web.whatsapp.com/send?phone={number}&text={message}'
        sent = False
        for i in range(3):  # Retry 3 times if needed
            if not sent:
                driver.get(url)
                try:
                    # Wait for the "Send" button to be clickable
                    click_btn = WebDriverWait(driver, delay).until(
                        EC.element_to_be_clickable((By.XPATH, "//button[@aria-label='Send']"))
                    )
                except Exception as e:
                    print(style.RED + f"\nFailed to send message to: {number}, retry ({i + 1}/3)")
                    print("Make sure your phone and computer are connected to the internet.")
                    print("If there is an alert, please dismiss it." + style.RESET)
                else:
                    sleep(1)
                    click_btn.click()
                    sent = True
                    sleep(3)
                    print(style.GREEN + 'Message sent to: ' + number + style.RESET)
                    sleep(wait_time_between_messages)  # Wait before sending the next message
    except Exception as e:
        print(style.RED + f'Failed to send message to {number}: {e}' + style.RESET)


# Close the browser once all messages are sent
driver.quit()