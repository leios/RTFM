#!/usr/bin/env python2

#-------------dialogue.py------------------------------------------------------#
#
# Purpose: do all text-based operation for RTFM
#------------------------------------------------------------------------------#

import curses, time
from input import *
from init import *

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

def print_code(codebox, line, sleep_time, code_line):
    # find size of codebox
    (cbrows, cbcols) = codebox.getmaxyx()

    time.sleep(sleep_time)

    if type(line) == str:
        codebox.addstr(code_line,0, line)
        codebox.refresh()
        code_line = code_line + 1
        return code_line
    elif type(line) == list:
        for i in range(0, cbrows - 1):
            print_code(codebox, line[- cbrows + i - code_line], 0, i)

