"""
on mac os make sure under Security&Privacy > Accessibility > Privacy (TAB) > PyCharm allow app to control computer
"""
import pywhatkit
import pyautogui as pg
pywhatkit.sendwhatmsg_instantly('+49xxxxx', 'Testing pywhatkit', wait_time=6, tab_close=False)
