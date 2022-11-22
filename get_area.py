import tkinter as tk

#coordinates
def get_drawing_area_coordinates():
    coords = [0,0,0,0] # coordinates => [start_x, start_y, end_x, end_y]

    #create window and canvas
    window = tk.Tk()
    canvas = tk.Canvas(window, cursor="tcross")

    #pack the canvas and fill
    canvas.pack(fill=tk.BOTH, expand=True)

    #create rectangle for selection
    rect = canvas.create_rectangle(0, 0, 0, 0, fill="red", outline="red")

    #set the window's attributes fullscreen and transparent
    window.attributes("-fullscreen", True)
    window.attributes("-alpha", 0.1)

    #get coordinates where mouse button 1 pressed
    def get_start_positions(event):
        coords[0], coords[1] = event.x, event.y

    #get coordinates where mouse button 1 released
    def get_end_positions(event):
        coords[2], coords[3] = event.x, event.y
        window.destroy()

    #when mouse moved update selection area
    def get_current_positions(event):
        canvas.coords(rect, coords[0], coords[1], event.x, event.y)

    #bind mouse events
    window.bind("<Button-1>", get_start_positions)
    window.bind("<ButtonRelease-1>", get_end_positions)
    window.bind("<B1-Motion>", get_current_positions)

    window.mainloop()

    #return coordinates
    return coords
