#!/usr/bin/env python

import curses
import curses.textpad
import random
import time

SEED_VAL = 50  # percent change of LIFE
ICON = 'o'
BLANK = ' '


def next_generation(matrix):

    # reset and clear
    matrix_2 = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):

            neighbors = 0
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if i >= 0 and i < len(matrix[0]) and \
                       j >= 0 and j < len(matrix):
                        if not (j == y and i == x):
                            if matrix[j][i] == 1:
                                neighbors += 1

            # matrix_2[y][x] = neighbors

            # the rules
            if matrix[y][x] == 0 and neighbors == 3:
                 matrix_2[y][x] = 1

            elif matrix[y][x] == 1 and (neighbors == 2 or
                                        neighbors == 3):
                 matrix_2[y][x] = 1

            elif matrix[y][x] == 1 and (neighbors > 3 or neighbors < 2):
                 matrix_2[y][x] = 0

    # matrix_print(matrix_2)
    return matrix_2


def draw(screen, matrix):
    # screen.clear()
    height, width = screen.getmaxyx()

    # corners
    screen.addch(0, 0, curses.ACS_ULCORNER)
    screen.addch(0, width - 1, curses.ACS_URCORNER)
    screen.addch(height - 1, 0, curses.ACS_LLCORNER)
    try:
        screen.addch(height - 1, width - 1, curses.ACS_LRCORNER)
    except curses.error:
        pass

    # borders
    for x in range(1, width - 1):
        screen.addch(0, x, curses.ACS_HLINE)
    for x in range(1, width - 1):
        screen.addch(height - 1, x, curses.ACS_HLINE)
    for y in range(1, height - 1):
        screen.addch(y, 0, curses.ACS_VLINE)
    for y in range(1, height - 1):
        screen.addch(y, width - 1, curses.ACS_VLINE)

    # grid
    for y in range(1, len(matrix) - 1):
        for x in range(1, len(matrix[0]) - 1):
            if y < height and x < width - 1:
                if matrix[y][x] == 1:
                    screen.addch(y, x, ICON)
                else:
                    screen.addch(y, x, BLANK)


def seed(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if random.randint(0, 100) > SEED_VAL:
                matrix[y][x] = 1


def matrix_print(matrix):
    for row in matrix:
        print(row)


def main(screen=None):
    # curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)

    if screen:
        height, width = screen.getmaxyx()
    else:
        height, width = 10, 10

    matrix = [[0 for x in range(width)] for y in range(height)]
    seed(matrix)

    if screen:
        draw(screen, matrix)
        screen.refresh()
        while True:
            # ch = screen.getch()
            # if ch == ord('q'):
            #     break
            matrix = next_generation(matrix)
            # matrix, matrix_2 = matrix_2, matrix
            draw(screen, matrix)
            screen.refresh()
            time.sleep(0.25)
    else:
        for _ in range(3):
            matrix_print(matrix)
            print()
            matrix = next_generation(matrix)

if __name__ == "__main__":
    # main()
    curses.wrapper(main)
