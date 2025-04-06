"""
File: DoubleBeepers.py
Name: 鍾念庭
-------------------------------
TODO:
"""

from karel.stanfordkarel import *


def main():
    """
    Karel will double the beepers
    """
    pass
    while front_is_clear():
        if on_beeper():
            double_beepers()
        move()

    # Return to the initial position
    go_home()


def double_beepers():
    # move beepers to the row above
    while on_beeper():
        pick_beeper()
        move_up()
        put_beeper()
        move_down()

    # move to the row above
    move_up()

    # move beepers back to the first row and double the beepers
    while on_beeper():
        pick_beeper()
        move_down()
        for i in range(2):
            put_beeper()
        move_up()

    # return to the first row
    move_down()


def move_up():
    """
    pre-condition: Karel is on the first row, facing East
    post-condition: Karel is on the above row, facing North
    """
    turn_left()
    move()


def move_down():
    """
    pre-condition: Karel is on the above row, facing North
    post-condition: Karel is on the first row, facing East
    """
    turn_around()
    move()
    turn_left()


def turn_around():
    turn_left()
    turn_left()


def go_home():
    """
    return Karel to the southwest corner and face East
    """
    turn_around()
    while front_is_clear():
        move()
    turn_around()






# ----- DO NOT MODIFY CODE BELOW THIS LINE ----- #
if __name__ == '__main__':
    execute_karel_task(main)
