#!/usr/bin/env python2

#-------------init.py----------------------------------------------------------#
# 
# Purpose: initializes textbox, bg screen, and codebox
#------------------------------------------------------------------------------#

import curses, time
from input import *
from dialogue import *

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
    cb_h = rows -  4
    cb_w = cols
    cb_x = 0
    cb_y = 0
    
    codebox = curses.newwin(cb_h, cb_w, cb_y, cb_x)
    
    #codebox.addstr(1,2, "Hey, this is a test codebox")
    codebox.refresh()
    
    # pause for a second
    return codebox

