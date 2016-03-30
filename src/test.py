#!/usr/bin/env python2

#-------------test.py----------------------------------------------------------#
#
# Purpose: To test basic code and textbox functions for RTFM
#------------------------------------------------------------------------------#

import curses, time
from input import *
from init import *
from dialogue import *

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

