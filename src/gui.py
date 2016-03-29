#!/usr/bin/env python2

#-------------gui.py-----------------------------------------------------------#
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

import curses
import time

# Set up standard screen
def init_bg():
    bg = curses.initscr()
    curses.start_color()
    curses.use_default_colors()
    
    for i in range(0, curses.COLORS):
        curses.init_pair(i, i, -1)
    
    # Inhibits typing to screen
    curses.noecho()
    
    # No need for enter to use commands
    curses.cbreak()
    
    # Setting up keypad usage
    bg.keypad(1)
    return bg

# Initializes textbox at bottom 4 rows and all columns
def init_textbox(bg):
    # Finding the number of columns and rows in the terminal
    (rows, cols) = bg.getmaxyx()
    
    # Adds in a new window for textbox
    tb_h = 4 
    tb_w = cols
    tb_x = 0
    tb_y = rows - 4
    
    textbox = curses.newwin(tb_h, tb_w, tb_y, tb_x)
    
    # define border on textbox
    textbox.border()
    
    textbox.move(1,1)
    
    #textbox.addstr(1,2, "Hey, this is a test textbox")
    textbox.refresh()
    
    # pause for a second
    return textbox

def init_codebox(bg):
    # Finding the number of columns and rows in the terminal
    (rows, cols) = bg.getmaxyx()
    
    # Adds in a new window for codebox
    cb_h = rows - 4 
    cb_w = cols
    cb_x = 0
    cb_y = 0
    
    codebox = curses.newwin(cb_h, cb_w, cb_y, cb_x)
    
    #codebox.addstr(1,2, "Hey, this is a test codebox")
    codebox.refresh()
    
    # pause for a second
    return codebox

# Places dialogue in textbox
# sleep_time is the amount of time that the dialog waits after every word for
# readibility... Can be turned off if 0.
def dialogue(textbox, text, sleep_time):

    # finds size of textbox
    (tbrows, tbcols) = textbox.getmaxyx()

    # clears textbox CHECK: functionize?
    for i in range(2, tbcols - 2):
        textbox.addch(1, i, " ")
        textbox.addch(2, i, " ")

    words = text.split()

    # word wrapping 
    # wordcols is the current column to place words
    # row_num is the row at which we are currently writing
    wordcols = 2
    row_num = 1
    for word in words:
        wordcols = wordcols + len(word + " ")
        if (word == '\\n'):
            # newlines will add columns to the end so that we change lines in
            # the next if condition block
            wordcols = tbcols
        else:
            if wordcols < tbcols - 2:
                textbox.addstr(row_num, wordcols - len(word + " "), word + " ")
                textbox.refresh()
                time.sleep(sleep_time)
            else:
                # additional command necessary to proceed, if we are at row 2
                if row_num == 2:
                    # waits for command
                    continue_text(textbox, tbcols)
                    row_num = 1
                else:
                    row_num = 2
                wordcols = 2
                textbox.addstr(row_num, wordcols, word + " ")
                wordcols = wordcols + len(word + " ")
                textbox.refresh()
                time.sleep(sleep_time)

    textbox.refresh()

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

def print_code(codebox, line, sleep_time, code_line):
    codebox.addstr(code_line,0, line)
    codebox.refresh()
    time.sleep(sleep_time)
    code_line = code_line + 1
    return code_line

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

# Clears curses
def kill_curses(bg, textbox):
    # finds size of textbox
    (tbrows, tbcols) = textbox.getmaxyx()

    # Requesting user input before stopping
    dialogue(textbox, "press SPACE to end", 0)
    continue_text(textbox, tbcols)
    
    # Terminating curses:
    curses.nocbreak()
    bg.keypad(0)
    curses.echo()
    curses.endwin()

'''
#------------------------------------------------------------------------------#
# MAIN
#------------------------------------------------------------------------------#

bg = init_bg()
textbox = init_textbox(bg)
codebox = init_codebox(bg)

text = "One day, I was sitting at home, drinking coffee, when I thought to myself, 'hey, I look a lot like that one guy,' but then I realized that I am actually not that guy. I am me. That was a sad day."

dialogue(textbox, text, .1)

line = "yo yo yo."
code_line = 0
code_line = print_code(codebox,line, 0.1, code_line)
time.sleep(2)
kill_curses(bg)
'''
