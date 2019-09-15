from pyautogui import hotkey
import time
import random

import configs


def AntiIdle():
	while True:
		if configs.runProgram:
			DirectionChoices = ['up', 'down', 'left', 'right']

			Direction = random.choice(DirectionChoices)

			hotkey('ctrl', Direction)

			time.sleep(3)
		else:
			time.sleep(3)


if __name__ == '__main__':
	AntiIdle()