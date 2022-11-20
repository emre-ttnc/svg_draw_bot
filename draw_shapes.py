from mouse import press, move, release


def draw_line(x1:float, y1:float, x2:float, y2:float):
    move(x1, y1, absolute=True, duration=0) #go to start point
    press(button="left")
    move(x2, y2, absolute=True, duration=0.2) #go to end point
    release(button="left")

def draw_rect(x:float, y:float, width:float, height:float):
    move(x, y, absolute=True, duration=0) #go to start point
    press(button="left")
    move(x+width, y, absolute=True, duration=0.2) #go to top-right
    move(x+width, y+height, absolute=True, duration=0.2) #go to bottom-right
    move(x, y+height, absolute=True, duration=0.2) #go to bottom-left
    move(x, y, absolute=True, duration=0.2) #return start point
    release(button="left")

def draw_polygon(x, y, scale_rate, points):
    move(x+float(points[0])*scale_rate, y+float(points[1])*scale_rate, absolute=True, duration=0) #go to start point
    press(button="left")
    for i in range(2, len(points), 2): #step 2 because points = (x1, y1, x2, y2, x3, y3, ...)
        move(x+float(points[i])*scale_rate, y+float(points[i+1])*scale_rate, absolute=True, duration=0.2) #go to next point
    move(x+float(points[0])*scale_rate, y+float(points[1])*scale_rate, absolute=True, duration=0.2) #return start point
    release(button="left")

def draw_polyline(x, y, scale_rate, points):
    move(x+float(points[0])*scale_rate, y+float(points[1])*scale_rate, absolute=True, duration=0) #go to start point
    press(button="left")
    for i in range(2, len(points), 2): #step 2 because points = (x1, y1, x2, y2, x3, y3, ...)
        move(x+float(points[i])*scale_rate, y+float(points[i+1])*scale_rate, absolute=True, duration=0.2) #go to next point
    release(button="left")