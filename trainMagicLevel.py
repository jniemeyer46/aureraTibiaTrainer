from pyautogui import press
import time

import configs


def TrainMagicLevel():
	while True:
		if configs.runProgram:
			press('f8')

			time.sleep(3)
		else:
			time.sleep(3)


if __name__ == '__main__':
	TrainMagicLevel()
