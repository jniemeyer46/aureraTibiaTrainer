from pyautogui import click
import time

import configs


def EatFood():
	while True:
		if configs.runProgram:
			click(button = 'right', x=1772, y=535)

			time.sleep(10)
		else:
			time.sleep(10)


if __name__ == '__main__':
	EatFood()