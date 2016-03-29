#!/usr/bin/env python2

#-------------code_parser.py---------------------------------------------------#
# 
# Purpose: to parse code for the RTFM "game."
#
#   Notes: This may end up being merged with gui.py
#          Small graphical bug when scrolling while writing, line removed, 
#             before being written
#
#------------------------------------------------------------------------------#

import curses, time
from input import *
from init import *
from dialogue import *

def parse(filename, textbox, codebox, sleep_time):
    code = open(filename, "r")
    code_line = 0

    # find size of codebox
    (cbrows, cbcols) = codebox.getmaxyx()

    # creates the list of lines on screen
    line_list = []

    # finds size of textbox
    (tbrows, tbcols) = textbox.getmaxyx()

    for line in code:
        if (line.startswith("$$")):
            dialogue(textbox, line[2:], sleep_time)
            continue_text(textbox, tbcols)
        else:
            # Set to -2 for now; however, I would like to eventually remove
            # the whitespace at the bottom of the codebox
            # code_line set to 0, so we always grab bottom of file
            if code_line > cbrows - 2:
                line_list.append(line)
                print_code(codebox, line_list, sleep_time, 0)
            else:
                code_line = print_code(codebox, line, sleep_time, code_line)
                line_list.append(line)
             
    return line_list

#------------------------------------------------------------------------------#
# MAIN
#------------------------------------------------------------------------------#

# initializes screen and everything
bg = init_bg()
textbox = init_textbox(bg)
codebox = init_codebox(bg)

line_list = parse("example_2.cpp", textbox, codebox, 0.1) 
browse_code(textbox, codebox, bg, line_list, 0.1)
#kill_curses(bg, textbox)
