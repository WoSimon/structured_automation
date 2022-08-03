import time
import pyautogui as pg

time.sleep(3)
pg.click(x=841, y=93)


def create_task(name, length_mins):
    # Open the create new task window
    pg.keyDown('command')
    pg.press('n')

    # Enter the name of the task
    pg.keyUp('command')
    pg.write(name)
    pg.press('enter')
    time.sleep(1)

    # Click more options
    pg.click(x=1118, y=600)
    time.sleep(1)

    # Enter the length of the task
    hrs = length_mins // 60
    mins = length_mins % 60
    print(hrs, mins)
    pg.doubleClick(x=970, y=425)
    pg.keyDown('command')
    pg.keyDown('shift')
    pg.press('left')
    pg.keyUp('command')
    pg.keyUp('shift')
    pg.press('backspace')
    pg.write(str(hrs))
    time.sleep(1)
    pg.doubleClick(x=1075, y=426)
    pg.keyDown('command')
    pg.keyDown('shift')
    pg.press('left')
    pg.keyUp('command')
    pg.keyUp('shift')
    pg.press('backspace')
    pg.write(str(mins))
    time.sleep(1)
    pg.press('enter')
    pg.press('enter')


# create_task(name='Test', length_mins=60)
