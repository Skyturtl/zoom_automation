import schedule
import time
import os
import pyautogui

def find_img(img):
    try:
        return pyautogui.locateOnScreen(img, grayscale=True, confidence=0.9)
    except pyautogui.ImageNotFoundException:
        return None

def open_zoom_and_mute():
    https_link = "Your_Zoom_Link_Here"
    zoom_link = https_link.replace("https://", "zoommtg://").replace("/j/", "/join?action=join&confno=")
    os.system(f'start "" "{zoom_link}"')

    join_button = None
    while True:
        join_button = find_img("join.png")
        if join_button:
            pyautogui.click(join_button)
            break
        time.sleep(3)

    audio_button = None
    while True:
        audio_button = find_img("audio.png")
        if audio_button:
            pyautogui.click(audio_button)
            break
        time.sleep(3)

# Day must be in lowercase and full name (e.g., "monday", "tuesday", etc.), and time in "HH:MM" 24-hour format
# Multiple schedules can be added as needed
schedule.every().wednesday.at("HH:MM").do(open_zoom_and_mute)

while True:
    schedule.run_pending()
    time.sleep(1)