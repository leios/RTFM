#!/usr/bin/env python2

#-------------code_parser.py---------------------------------------------------#
# 
# Purpose: to parse code for the RTFM "game."
#
#   Notes: This may end up being merged with gui.py
#
#------------------------------------------------------------------------------#

from gui import *

def parse(filename, textbox, codebox, sleep_time):
    code = open(filename, "r")
    code_line = 0

    # finds size of textbox
    (tbrows, tbcols) = textbox.getmaxyx()

    for line in code:
        if (line.startswith("$$")):
            dialogue(textbox, line[2:], sleep_time)
            continue_text(textbox, tbcols)
        else:
            code_line = print_code(codebox, line, sleep_time, code_line)

#------------------------------------------------------------------------------#
# MAIN
#------------------------------------------------------------------------------#

# initializes screen and everything
bg = init_bg()
textbox = init_textbox(bg)
codebox = init_codebox(bg)

parse("example.py", textbox, codebox, 0.1) 
kill_curses(bg, textbox)
