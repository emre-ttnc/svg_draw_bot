from mouse import press, move, release
from math import sin, cos, pi

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

### x, y = center coordinate ### rx, ry = radius x, radius y ###
def draw_elliptical_arc(x, y, start_angle, end_angle, rx, ry):
    move(
        x + rx * round(sin(start_angle*pi/180), 5), 
        y + ry * round(cos(start_angle*pi/180), 5), 
        absolute=True, duration=0) #go to start point
    press(button="left")
    for angle in range(start_angle, end_angle+1, 3): # reduce the step for smoother edges
        pos_x = x + rx * round(sin(angle*pi/180), 5)
        pos_y = y + ry * round(cos(angle*pi/180), 5)
        move(pos_x, pos_y, absolute=True, duration=0.005) #decrase/incrase the step/duration for speed.
    release(button="left")

def draw_arc(x, y, start_angle, end_angle, r):
    draw_elliptical_arc(x=x, y=y, start_angle=start_angle, end_angle=end_angle, rx=r, ry=r)

def draw_ellipse(cx, cy, rx, ry): #draw elliptical arc from 0 to 360
    draw_elliptical_arc(x=cx, y=cy, start_angle=0, end_angle=360, rx=rx, ry=ry)

def draw_circle(cx, cy, r):  #draw arc from 0 to 360
    draw_arc(x=cx, y=cy, start_angle=0, end_angle=360, r=r)
