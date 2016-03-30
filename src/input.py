#!/usr/bin/env python2

#-------------input.py---------------------------------------------------------#
#
# Purpose: Generate a textbox for the RTFM "game"
#
#   Notes: uses curses -- use python2.7, python3 is unstable.
#          This file will create the dialog box for regular play, but will not
#              create the additional ascii graphics for the upper window.
#          Regular play is actually just scripting on a terminal, so we need 
#              some way of flipping from this screen to vim or the appropriate
#              IDE... I don't know how to do this...
#
#------------------------------------------------------------------------------#

import curses, time
from input import *
from dialogue import *

def continue_text(textbox, cols):
    # flush input from buffer
    curses.flushinp()

    # indicates button to press:
    button = "PRESS SPACE"
    textbox.addstr(3, cols - 2 - len(button), button)

    # waits for command
    while True:
        textcomm = textbox.getch()
        if textcomm == ord(" "):
            break

    # clears text
    clear_text(textbox, cols)

    # remove button indication
    for i in range(len(button)):
        textbox.addch(3, cols - 2 - len(button) + i, curses.ACS_HLINE)

# clears codebox
def clear_code(codebox):
    # finds size of codebox
    (cbrows, cbcols) = codebox.getmaxyx()

    # clears codebox CHECK: functionize?
    for i in range(0, cbrows):
        for j in range(0, cbcols-1):
            codebox.addch(i, j, " ")
    codebox.refresh()

# clears textbox
def clear_text(textbox, cols):
    # clears textbox
    for i in range(2, cols - 2):
        textbox.addch(1, i, " ")
        textbox.addch(2, i, " ")

# Allows user to analyze code at end
def browse_code(textbox, codebox, bg, line_list, sleep_time):
    # Find size of textbox and codebox
    (cbrows, cbcols) = codebox.getmaxyx()
    (tbrows, tbcols) = textbox.getmaxyx()

    # Requesting user input before stopping
    dialogue(textbox, 
             "press SPACE to end \\n press UP to go up and DOWN to go down", 0)

    # request user input for moving up and down on the screen
    index = 0
    while True:
        browser = textbox.getch()
        if browser == ord(" "):
            kill_curses(bg)
            break
        if browser == ord("w"):
            index = index + 1
            if cbrows + index > len(line_list):
                index = index - 1
            print_code(codebox, line_list, sleep_time, index)
        if browser == ord("s"):
            index = index - 1
            if index < 0:
                index = 0
            print_code(codebox, line_list, sleep_time, index)

# Clears curses
def kill_curses(bg):

    # Terminating curses:
    curses.nocbreak()
    bg.keypad(0)
    curses.echo()
    curses.endwin()

