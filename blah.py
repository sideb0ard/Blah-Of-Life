#!/usr/bin/env python

import curses
import curses.textpad
import random
import sys
import time

SEED_VAL = 50  # percent change of LIFE
ICON = '#'
BLANK = ' '
DELAY = 0.25


class Node:

    def __init__(self, color=None):
        self.age = 0
        self.color = color

    def age_inc(self):
        self.age += 1

    def age_get(self):
        return self.age

    def color_get(self):
        return self.color


def biggest(*argv):
    num_numz = len(argv)
    biggest = 0
    if num_numz > 1:
        while (num_numz > 1):
            if int(argv[num_numz - 1]) > biggest:
                biggest = int(argv[num_numz - 1])
            num_numz -= 1

    return biggest


def next_generation(matrix):

    # reset and clear
    matrix_2 = [[None for x in range(len(matrix[0]))] for y in
                range(len(matrix))]

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):

            neighbors = 0
            color_a = 0
            color_b = 0
            color_c = 0
            color_d = 0
            for i in range(x - 1, x + 2):
                for j in range(y - 1, y + 2):
                    if i >= 0 and i < len(matrix[0]) and \
                       j >= 0 and j < len(matrix):
                        if not (j == y and i == x):
                            if matrix[j][i]:
                                neighbors += 1
                                if matrix[j][i].color_get() == 2:
                                    color_a += 1
                                if matrix[j][i].color_get() == 3:
                                    color_b += 1
                                if matrix[j][i].color_get() == 4:
                                    color_c += 1
                                else:
                                    color_d += 1

            biggy = biggest(color_a, color_b, color_c, color_d)
            if biggy == color_a:
                dominant_color = 2
            elif biggy == color_b:
                dominant_color = 3
            elif biggy == color_c:
                dominant_color = 4
            else:
                dominant_color = 5
            # matrix_2[y][x] = neighbors

            # the rules
            if matrix[y][x] is None and (neighbors == 3 or neighbors == 6):
                matrix_2[y][x] = Node(dominant_color)

            elif matrix[y][x] is not None and (neighbors == 2 or
                                               neighbors == 3):
                 matrix_2[y][x] = matrix[y][x]

            elif matrix[y][x] is not None and (neighbors > 3 or neighbors < 2):
                 matrix_2[y][x] = None

    # matrix_print(matrix_2)
    return matrix_2


def draw(screen, matrix):
    # screen.clear()
    height, width = screen.getmaxyx()

    # corners
    screen.addch(0, 0, curses.ACS_ULCORNER, curses.color_pair(2))
    screen.addch(0, width - 1, curses.ACS_URCORNER, curses.color_pair(2))
    screen.addch(height - 1, 0, curses.ACS_LLCORNER, curses.color_pair(2))
    try:
        screen.addch(height - 1, width - 1, curses.ACS_LRCORNER,
                     curses.color_pair(2))
    except curses.error:
        pass

    # borders
    for x in range(1, width - 1):
        screen.addch(0, x, curses.ACS_HLINE, curses.color_pair(1))
    for x in range(1, width - 1):
        screen.addch(height - 1, x, curses.ACS_HLINE, curses.color_pair(1))
    for y in range(1, height - 1):
        screen.addch(y, 0, curses.ACS_VLINE, curses.color_pair(1))
    for y in range(1, height - 1):
        screen.addch(y, width - 1, curses.ACS_VLINE, curses.color_pair(1))

    # grid
    for y in range(1, len(matrix) - 1):
        for x in range(1, len(matrix[0]) - 1):
            if y < height and x < width - 1:
                if matrix[y][x]:  # == 1:
                    screen.addch(y, x, ICON, curses.color_pair(matrix[y][x].
                                                               color_get()))
                else:
                    screen.addch(y, x, BLANK)


def seed(matrix):
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if random.randint(0, 100) > SEED_VAL:
                color = random.randint(2, 6)
                matrix[y][x] = Node(color)


def matrix_print(matrix):
    for row in matrix:
        print(row)


def main(screen=None):
    curses.init_pair(1, curses.COLOR_WHITE, curses.COLOR_BLACK)
    curses.init_pair(2, 54, curses.COLOR_BLACK)
    curses.init_pair(3, 125, curses.COLOR_BLACK)
    curses.init_pair(4, 153, curses.COLOR_BLACK)
    curses.init_pair(5, 254, curses.COLOR_BLACK)

    if screen:
        height, width = screen.getmaxyx()
    else:
        height, width = 10, 10

    matrix = [[None for x in range(width)] for y in range(height)]
    seed(matrix)

    if screen:
        screen.nodelay(1)
        draw(screen, matrix)
        screen.refresh()
        while True:
            ch = screen.getch()
            if ch == ord('q'):
                break
            matrix = next_generation(matrix)
            # matrix, matrix_2 = matrix_2, matrix
            draw(screen, matrix)
            screen.refresh()
            time.sleep(DELAY)
    else:
        for _ in range(3):
            matrix_print(matrix)
            print()
            matrix = next_generation(matrix)

if __name__ == "__main__":
    if len(sys.argv) > 1:
        DELAY = sys.argv[1]
    # main()
    curses.wrapper(main)
