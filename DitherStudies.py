import sys

WIDTH = 80
HEIGHT = 24

DITHERS = {
    "Floyd-Steinberg" :
            { "start_x" : 1,
            "start_y" : 0,
            "coef" : [[0, 0, 7 / 16], [3 / 16, 5 / 16, 1 / 16]]},
    "Zhigang Fan" :
            { "start_x" : 2,
            "start_y" : 0,
            "coef" : [[0, 0, 0, 7 / 48, 5 / 48], [1 / 16, 5 / 48, 7 / 48, 5 / 48, 1 / 16], [1 / 48, 1 / 16, 5 / 48, 1 / 16, 1 / 48]]},
    "Shiau-Fan" :
            { "start_x" : 2,
            "start_y" : 0,
            "coef" : [[0, 0, 0, 1 / 2], [1 / 8, 1 / 8, 1 / 4, 0]]},
    "Shiau-Fan 2" :
            { "start_x" : 3,
            "start_y" : 0,
            "coef" : [[0, 0, 0, 0, 1 / 2], [1 / 16, 1 / 16, 1 / 8, 1 / 4, 0]]},
    "Jarvis, Judice and Ninke" :
            { "start_x" : 2,
            "start_y" : 0,
            "coef" : [[0, 0, 0, 7 / 48, 5 / 48], [1 / 16, 5 / 48, 7 / 48, 5 / 48, 1 / 16], [1 / 48, 1 / 16, 5 / 48, 1 / 16, 1 / 48]]},
    "Stucki" : 
            { "start_x" : 2,
            "start_y" : 0,
            "coef" : [[0, 0, 0, 4 / 21, 2 / 21], [1 / 21, 2 / 21, 4 / 21, 2 / 21, 1 / 21], [1 / 42, 1 / 21, 2 / 21, 1 / 21, 1 / 42]]},
    "Burkes" :
            { "start_x" : 2,
            "start_y" : 0,
            "coef" : [[0, 0, 0, 1 / 4, 1 / 8], [1 / 16, 1 / 8, 1 / 4, 1 / 8, 1 / 16]]},
    "Sierra" :
            { "start_x" : 2,
            "start_y" : 0,
            "coef" : [[0, 0, 0, 5 / 32, 3 / 32], [1 / 16, 1 / 8, 5 / 32, 1 / 8, 1 / 16], [0, 1 / 16, 3 / 32, 1 / 16, 0]]},
    "Two-Row Sierra" :
            { "start_x" : 2,
            "start_y" : 0,
            "coef" : [[0, 0, 0, 1 / 4, 3 / 16], [1 / 16, 1 / 18, 3 / 16, 1 / 8, 1 / 16]]},
    "FilterLite" :
            { "start_x" : 1,
            "start_y" : 0,
            "coef" : [[0, 0, 1 / 2], [1 / 4, 1 / 4, 0]]},
    "Atkinson" :
            { "start_x" : 1,
            "start_y" : 0,
            "coef" : [[0, 0, 1 / 8, 1 / 8], [1 / 8, 1 / 8, 1 / 8, 0], [0, 1 / 8, 0, 0]]}
}

class Ditherer(object):
    def __init__(self, dither, perc):
        self.matrix = [[perc for i in range(WIDTH)] for j in range(HEIGHT)]
        self.dithername = dither
        self.coefset = DITHERS[dither]['coef']
        self.start_x = DITHERS[dither]['start_x']
        self.start_y = DITHERS[dither]['start_y']

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
                if x_use >= 0 and y_use >= 0 and x_use < WIDTH and y_use < HEIGHT:
                    self.matrix[y_use][x_use] -= changeval * coef

    def draw(self):
        print(f'drawing {self.dithername}')
        for y in range(HEIGHT):
            for x in range(WIDTH):
                self.calculate_cell(x, y)
        for y in range(HEIGHT):
            for x in range(WIDTH):
                if self.matrix[y][x] == 1.0: whitecell()
                else: blackcell()
            if y == HEIGHT - 1: 
                wait() # if last line, wait for input, don't newline
            else: newline()

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

def blackcell():
    sys.stdout.write('\x1b[{0}m '.format(40))
def whitecell():
    sys.stdout.write('\x1b[{0}m '.format(47))
def newline():
    sys.stdout.write('\x1b[{0}m'.format(40)) #set to black in case there are remaining cells
    sys.stdout.write('\n')
def wait():
    sys.stdout.write('\x1b[{0}m'.format(40)) #set to black in case there are remaining cells
    input()

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
        ditherer = Ditherer(d, p / 100)
        ditherer.draw()
    
if __name__ == '__main__':
    main()
