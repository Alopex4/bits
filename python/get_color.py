#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# [src](https://github.com/reorx/python-terminal-color/blob/master/color_simple.py)
r""" 
Simple color code snip.

[usage]
    red('hello world')
"""

import sys

# check is tty like `fd` or not
ISATTY = sys.stdout.isatty()


def make_color(code):
    def color_func(s):
        if not ISATTY:
            return s
        tpl = '\x1b[{}m{}\x1b[0m'
        return tpl.format(code, s)
    return color_func


# format
bold = make_color(1)
underline = make_color(4)

# color code
black = make_color(30)
red = make_color(31)
green = make_color(32)
yellow = make_color(33)
blue = make_color(34)
magenta = make_color(35)
cyan = make_color(36)
white = make_color(37)

# different grayscal
# \x1b[38;5;232m\x1b[0m `to` \x1b[38;5;255m\x1b[0m
# ok --> \x1b[38;5;255mok\x1b[0m
grayscale = {(i - 232): make_color('38;5;' + str(i)) for i in range(232, 256)}
