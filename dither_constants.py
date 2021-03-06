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