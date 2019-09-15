from checkButtonPress import CheckButtonPress
from trainMagicLevel import TrainMagicLevel
from antiIdle import AntiIdle
from eatFood import EatFood
from login import LoginAndSetup
from checkTime import CheckTime
import configs

from pynput import keyboard
import threading
import time


''' Thread Class Definition '''
class myThread(threading.Thread):
	def __init__(self, ThreadID, ThreadName, ThreadAction):
		threading.Thread.__init__(self)
		self.ThreadID = ThreadID
		self.ThreadName = ThreadName
		self.ThreadAction = ThreadAction

	def run(self):
		print("Spinning up a thread for the " + self.ThreadName + " bot functionality.")
		self.ThreadAction()


def main():
	# Define the possible actions
	threadNames = ['Check-button-press', 'Check-Time', 'Anti-Idle', 'Eat-Food', 'Train-Magic-Level']
	threadActions = [CheckButtonPress, CheckTime, AntiIdle, EatFood, TrainMagicLevel]
	threads = []
	threadID = 0

	for tName in threadNames:
		thread = myThread(threadID, tName, threadActions[threadID])
		thread.start()
		threads.append(thread)
		threadID += 1


if __name__ == '__main__':
	main()