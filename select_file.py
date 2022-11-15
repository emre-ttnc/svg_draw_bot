from tkinter import Tk
from tkinter.filedialog import askopenfilename

def get_lines():
    Tk().withdraw()

    file = askopenfilename(filetypes=[("SVG Files",["svg"])])

    if file:
        with open(file,"r") as svg_file:
            lines = svg_file.readlines()
            return lines