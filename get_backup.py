import pyautogui as pg
import time


def get_data():
    # Activate the window
    time.sleep(2)
    pg.click(x=841, y=93)

    # Open Settings
    pg.keyDown('command')
    pg.press(',')
    pg.keyUp('command')

    # Click Advanced
    time.sleep(1)
    pg.click(x=550, y=538)

    # Click Backup
    time.sleep(1)
    pg.click(x=541, y=329)

    # Click Start Backup
    time.sleep(1)
    pg.click(x=518, y=330)

    # Navigate out of the settings window
    time.sleep(1)
    pg.click(x=466, y=164)
    time.sleep(1)
    pg.click(x=466, y=164)
    time.sleep(1)
    pg.click(x=948, y=162)


get_data()
