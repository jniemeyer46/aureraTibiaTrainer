from pyautogui import click, typewrite, press
import time
import configs


def LoginAndSetup():

    click(x=102, y=833)

    typewrite(configs.accountName)
    
    press('tab')
    
    typewrite(configs.password)

    press('enter')
    time.sleep(1) 
    press('enter')
    time.sleep(1)

    click(button='right', x=956, y=368)
    time.sleep(1)
    click(button='right', x=1849, y=176)
    time.sleep(1)
    click(button='right', x=1766, y=536)


if __name__ == '__main__':
	LoginAndSetup()