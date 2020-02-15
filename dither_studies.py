import sys
import os
import curses
from dither_constants import DITHERS

class Ditherer(object):
    def __init__(self, dither, perc, height, width):
        self.matrix = [[perc * .01 for i in range(width)] for j in range(height)]
        self.dithername = dither
        self.coefset = DITHERS[dither]['coef']
        self.start_x = DITHERS[dither]['start_x']
        self.start_y = DITHERS[dither]['start_y']
        self.width = width
        self.height = height

    def calculate_cell(self, x, y):
        oldval = self.matrix[y][x]
        self.matrix[y][x] = 0 if oldval < .5 else 1
        changeval = self.matrix[y][x] - oldval

        # loop through coefficients for the dither and carry over error
        # i:x,j:y where i.j are coeffs and x,y are matrix cells
        for j, yrow in enumerate(self.coefset):
            for i, coef in enumerate(yrow):
                x_use = x + i - self.start_x
                y_use = y + j - self.start_y
                if x_use >= 0 and y_use >= 0 and x_use < self.width and y_use < self.height:
                    self.matrix[y_use][x_use] -= changeval * coef
                    
    def draw(self, stdscr):
        # calculate cells
        for y in range(self.height):
            for x in range(self.width):
                self.calculate_cell(x, y)

        # ready to draw
        stdscr.attron(curses.color_pair(2))
        for y in range(self.height):
            for x in range(self.width):
                if self.matrix[y][x] == 1.0: 
                    stdscr.addstr(y, x, " ")

def dither(stdscr, d, p):
    # Clear and refresh the screen for a blank canvas
    stdscr.clear()
    stdscr.refresh()

    # Start colors in curses
    curses.start_color()
    curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_BLACK) # no color
    curses.init_pair(2, curses.COLOR_BLACK, curses.COLOR_WHITE) # white background

    # initialize
    stdscr.clear()
    height, width = stdscr.getmaxyx()

    # actually draw the cells
    ditherer = Ditherer(d, p, height - 1, width - 1)
    ditherer.draw(stdscr)

    # Turn off attributes
    stdscr.attroff(curses.color_pair(2))

    # Refresh the screen
    stdscr.refresh()

    # Wait for input to clear
    stdscr.getch()

def get_input(min, max):
    is_valid = False
    while not is_valid:
        try:
            i = int(input('> '))
            if (min <= i <= max):
                is_valid = True
        except ValueError:
            is_valid = False
        if not is_valid:
            print(f'Invalid response, please enter a number between {min} and {max}')
    return i

def prompt():
    print("Choose a dither pattern:")
    for choice, key in enumerate(DITHERS):
        print(f'{choice}) {key}')
    d = get_input(0, len(DITHERS.keys()) - 1)
    dither = list(DITHERS.keys())[int(d)]
    print(f'You chose {dither}')

    print("\nChoose a %:")
    perc = get_input(0, 100)
    return dither, perc

def main():
    while(True):
        d, p = prompt()
        curses.wrapper(dither, d, p)

if __name__ == "__main__":
    main()
