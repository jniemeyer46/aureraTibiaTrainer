import pyautogui
import time

import configs
from pynput import keyboard


def CheckButtonPress():
    with keyboard.Listener(on_press=on_press) as listener:
        while True:
            pass


def on_press(key):
    if key == keyboard.Key.home:
        if configs.runProgram:
            print('The command to stop the program has been recieved: %s' % key)

            configs.runProgram = False
        elif not configs.runProgram:
            print('The program is starting up now')

            configs.runProgram = True


if __name__ == '__main__':
    checkForStartStopButtonPress(False)