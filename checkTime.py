from time import strftime, localtime, sleep
from login import LoginAndSetup
import configs


def CheckTime():
    while True:
        currentTime = strftime("%H:%M", localtime()).split(':')
        hour = int(currentTime[0])
        minute = int(currentTime[1])

        if hour == 1 and minute == 59:
            if configs.runProgram:
                print('Time to get ready for the server reset, turning off the trainer now!')

                configs.runProgram = False
            else:
                print('The trainer is currently off, will start it up when the server is back up.')
        elif hour == 2 and minute == 5:
            if configs.runProgram:
                print('THIS NEEDS TO BE OFF FOR THE LOGIN AND SETUP STEP')

                configs.runProgram = False
            else:
                print('It is time to start the program back up and get my character logged in!')

            LoginAndSetup()
            configs.runProgram = True
        
        sleep(60)


if __name__ == '__main__':
    checkTime()