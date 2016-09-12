#!/usr/bin/env python

import curses
import curses.textpad
# import time

# stdscr = curses.initscr()
# curses.cbreak()
# curses.noecho()
# stdscr.keypad(1)


def update_scr(screen):
    height, width = screen.getmaxyx()
    # print(height, width)

    screen.addch(0, 0, curses.ACS_ULCORNER)
    screen.addch(0, width - 1, curses.ACS_URCORNER)
    screen.addch(height - 1, 0, curses.ACS_LLCORNER)
    try:
        screen.addch(height - 1, width - 1, curses.ACS_LRCORNER)
    except curses.error:
        pass

    for x in range(1, width - 1):
        screen.addch(0, x, curses.ACS_HLINE)
    for x in range(1, width - 1):
        screen.addch(height - 1, x, curses.ACS_HLINE)
    for y in range(1, height - 1):
        screen.addch(y, 0, curses.ACS_VLINE)
    for y in range(1, height - 1):
        screen.addch(y, width - 1, curses.ACS_VLINE)


def main(screen):

    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    update_scr(screen)

    while True:
        ch = screen.getch()
        if ch == ord('q'):
            break
        update_scr(screen)

if __name__ == "__main__":
    curses.wrapper(main)
