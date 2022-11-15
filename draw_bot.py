from sys import exit
from select_file import get_lines

lines = get_lines()

if lines is None:
    exit()