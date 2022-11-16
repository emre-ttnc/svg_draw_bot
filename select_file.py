from tkinter import Tk
from tkinter.filedialog import askopenfilename

def get_lines():
    #Create windowless Tk
    Tk().withdraw()

    #open file select dialog and assign to file
    file = askopenfilename(filetypes=[("SVG Files",["svg"])])

    #if file selected
    if file:
        with open(file,"r") as svg_file:
            lines = svg_file.readlines()
            return lines