"""
https://web.whatsapp.com/send?phone=+49xxx
https://web.whatsapp.com/send?phone=+49xxx
"""

import pywhatkit
from os.path import join as os_join

config = {"pfad":"\\Users\\thomas\\Documents\\data\\upwork\\whatsapp_send"}

with open(os_join(config['pfad'], 'input.csv'), 'r') as file:
    for line in file:
        data = [elem.strip() for elem in line.split(",")]
        pywhatkit.sendwhatmsg_instantly(data[1], f'Hello {data[0]}', wait_time=4, tab_close=True)




