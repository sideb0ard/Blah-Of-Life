#!/usr/bin/env python

import curses
import curses.textpad
import random
import time

SEED_VAL = 50  # percent change of LIFE
ICON = '#'


def next_generation(matrix, matrix_2):

    # reset and clear
    matrix_2 = [[0 for x in range(len(matrix[0]))] for y in range(len(matrix))]

    for y in range(1, len(matrix) - 2):
        for x in range(1, len(matrix[0]) - 2):

            # print("STARTN! ", matrix[y][x], "\n")
            neighbors = 0
            for i in range(x - 1, x + 1):
                for j in range(y - 1, y + 1):
                    if j != y and i != x:
                        if matrix[j][i] == "1":
                            neighbors += 1

            print("VALY: ", matrix[y][x], "\n")
            print("NEIGBS: ", neighbors, "\n")
            time.sleep(1)

            # the rules
            if matrix[y][x] == 0:  # and neighbors == 3:
                matrix_2[y][x] = 1
                # print("ALIVE! ", matrix[y][x], "\n")
            else:  # matrix[y][x] == 1:  # and (neighbors == 2 or neighbors == 3):
                matrix_2[y][x] = 1
                # print("STAYUNG ALIVE! ", matrix[y][x], "\n")
            # elif matrix[y][x] == 1 and (neighbors > 3 or neighbors < 2):
            #     matrix_2[y][x] = 0
            #     print("SLEEPY TIME!")
            #     time.sleep(1)
    print(matrix_2)
    time.sleep(2)


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
        for x in range(0, len(matrix[0]) - 1):
            if matrix[y][x] == "1":
                if y < (height - 1) and x < (width - 1):
                    screen.addch(y, x, ICON)


def seed(matrix):
    for y in range(1, len(matrix) - 1):
        for x in range(1, len(matrix[0]) - 1):
            if random.randint(0, 100) > SEED_VAL:
                matrix[y][x] = "1"


def main(screen):

    height, width = screen.getmaxyx()
    matrix = [[0 for x in range(width)] for y in range(height)]
    matrix_2 = [[0 for x in range(width)] for y in range(height)]
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLUE)
    seed(matrix)
    print(matrix)
    time.sleep(3)
    next_generation(matrix, matrix_2)
    matrix, matrix_2 = matrix_2, matrix
    print(matrix)
    time.sleep(3)

    # draw(screen, matrix)
    # screen.refresh()

    # while True:
    #     # ch = screen.getch()
    #     # if ch == ord('q'):
    #     #     break
    #     next_generation(matrix, matrix_2)
    #     matrix, matrix_2 = matrix_2, matrix
    #     draw(screen, matrix)
    #     screen.refresh()
    #     time.sleep(1)

if __name__ == "__main__":
    curses.wrapper(main)
