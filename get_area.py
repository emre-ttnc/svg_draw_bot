import tkinter as tk

#coordinates
sx, sy, ex, ey = 0,0,0,0

#create window and canvas
window = tk.Tk()
canvas = tk.Canvas(window, cursor="tcross")

#pack the canvas and fill
canvas.pack(fill=tk.BOTH, expand=True)

#create rectangle for selection
rect = canvas.create_rectangle(sx, sy, ex, ey, fill="red", outline="red")

#set the window's attributes fullscreen and transparent
window.attributes("-fullscreen", True)
window.attributes("-alpha", 0.1)

#get coordinates where mouse button 1 pressed
def get_start_positions(event):
    global sx
    global sy
    sx, sy = event.x, event.y

#get coordinates where mouse button 1 released
def get_end_positions(event):
    global ex
    global ey
    ex, ey = event.x, event.y
    window.destroy()

#when mouse moved update selection area
def get_current_positions(event):
    global ex
    global ey
    ex, ey = event.x, event.y
    canvas.coords(rect, sx, sy, ex, ey)

#bind mouse events
window.bind("<Button-1>", get_start_positions)
window.bind("<ButtonRelease-1>", get_end_positions)
window.bind("<B1-Motion>", get_current_positions)

window.mainloop()

#return coordinates with function
def get_positions():
    return sx, sy, ex, ey
