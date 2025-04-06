"""
File: BeeperRow.py
Name: 鍾念庭
-------------------------
This program makes Karel fill up
Street 1 with beepers
(This program should be world insensitive)
"""

from karel.stanfordkarel import *


def main():
    pass
    while front_is_clear():
        put_beeper()
        move()
    put_beeper()



# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
