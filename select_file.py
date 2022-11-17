from tkinter import Tk
from tkinter.filedialog import askopenfilename

def get_file_path():
    #Create windowless Tk
    Tk().withdraw()

    #open file select dialog and assign to file
    file = askopenfilename(filetypes=[("SVG Files",["svg"])])

    #if file selected
    if file:
        return file