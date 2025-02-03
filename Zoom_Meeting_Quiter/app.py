import pyautogui
import time

leave_time = "09:48"  # 24-hour format

while True:
    current_time = time.strftime("%H:%M")
    if current_time == leave_time:
        print("Leaving the meeting...")
        pyautogui.hotkey('alt', 'q')  # Windows/Linux
        # pyautogui.hotkey('command', 'w')  # macOS
        time.sleep(1)
        pyautogui.press('enter')  # Press 'Enter' to confirm
        break
    time.sleep(15)  # Check every 15 seconds

print("Meeting left successfully.")


