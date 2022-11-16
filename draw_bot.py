from sys import exit
from select_file import get_lines
from get_area import get_positions

#Get selected area coordinates
START_X, START_Y, END_X, END_Y = get_positions()

#if it is not an area then close the program
if START_X == END_X or START_Y == END_Y:
    exit()

#normalize coordinates if selected from the opposite direction
if START_X > END_X:
    START_X, END_X = END_X, START_X
if START_Y > END_Y:
    START_Y, END_Y = END_Y, START_Y

lines = get_lines()

#if get_lines function did not returned any data then close the program
if lines is None:
    exit()
