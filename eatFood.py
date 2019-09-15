from pyautogui import click
import time

import configs


def EatFood():
	while True:
		if configs.runProgram:
			click(button = 'right', x=1771, y=543)

			time.sleep(10)
		else:
			time.sleep(10)


if __name__ == '__main__':
	EatFood()