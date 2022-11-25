from mouse import press, move, release, drag, get_position
from math import sin, cos, pi
from time import sleep

def draw_line(x1:float, y1:float, x2:float, y2:float):
    drag(x1, y1, x2, y2, absolute=True, duration=0.2)

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

# parse path's d  (!)private method
def __parse_d(d: str):
    start_point = 0 # to keep position
    d = d.strip() # trim white spaces
    pieces = []
    for i in range(1, len(d)-1): # skip first char bc it should be "M" & skip last char bc it should be "Z" or number
        if d[i].upper() in ["M", "L", "H", "V", "C", "S", "Q", "T", "A", "Z"]:
            pieces.append(d[start_point:i])
            start_point = i
    # add last piece
    if d[-1].upper() == "Z":
        pieces.append(d[start_point:-1]) # add last piece without Z/z 
        pieces.append(d[-1]) # add z to pieces list
    else:
        pieces.append(d[start_point:]) # add last piece
    return pieces

# parse command  (!)private method
def __parse_command(main_piece: str):
    start_point = 1 #skip first char (command char)
    pieces = []
    main_piece = main_piece.strip() #trim white spaces
    if main_piece is None:
        return
    pieces.append(main_piece[0]) #add command char to list
    for i in range(1, len(main_piece)): #skip first char (command char)
        if main_piece[i] == "-":
            pieces.append(main_piece[start_point:i])
            start_point = i
        elif main_piece[i] in [",", " "]:
            pieces.append(main_piece[start_point:i])
            start_point = i+1
    # add last piece
    if main_piece[-1].upper() == "Z":
        pieces.append(main_piece[start_point:-1]) # add last piece without Z/z 
        pieces.append(main_piece[-1]) # add z to pieces list
    else:
        pieces.append(main_piece[start_point:]) # add last piece
    return list(filter(None, pieces))

# calc and move (cubic bézier) (!)private method
#sx, sy = start point ## dx1, dy1 = first reference point ## dx2, dy2 = second reference point ## dx,dy = end point
def __draw_cubic_bezier(sx, sy, dx1, dy1, dx2, dy2, dx, dy):
    for t in range(1, 26): #Increase the range for smoother line
        x = sx * (1-t/25)**3 + 3 * dx1 * t/25 * (1-t/25)**2 + 3 * dx2 * (t/25)**2 * (1 - t/25) + dx * (t/25)**3
        y = sy * (1-t/25)**3 + 3 * dy1 * t/25 * (1-t/25)**2 + 3 * dy2 * (t/25)**2 * (1 - t/25) + dy * (t/25)**3
        move(x, y, absolute=True, duration=0.01)

# calc and move (quadratic bézier) (!)private method
#sx, sy = start point ## dx1, dy1 = reference point ## dx,dy = end point
def __draw_quadratic_bezier(sx, sy, dx1, dy1, dx, dy):
    for t in range (1, 26): #Increase the range for smoother line
        x = sx * (1-t/25)**2 + 2 * dx1 * t/25 * (1-t/25) + dx * (t/25)**2
        y = sy * (1-t/25)**2 + 2 * dy1 * t/25 * (1-t/25) + dy * (t/25)**2
        move(x, y, absolute=True, duration=0.01)

def draw_path(d: str, x, y, scale_rate):
    pieces = __parse_d(d.strip())
    pieces = list(filter(None, pieces)) #remove empty pieces from pieces_list
    current_x, current_y = 0, 0 #for H and V command
    start_x, start_y = 0, 0 #for Z command
    mirror_x, mirror_y = 0, 0 #for smooth to (S-s) and T-t commands
    LINE_DURATION = 0.25 #for all line durations
    for piece in pieces:
        piece = piece.strip()
        if piece.strip().upper() != "Z": #if it is not "Z/z", parse command
            piece = __parse_command(piece)
        if piece is None:
            continue
        match piece[0]:
            case "M": #Move to point (absolute)
                release(button="left")
                move(x+float(piece[1])*scale_rate, y+float(piece[2])*scale_rate, absolute=True, duration=0) 
                press(button="left")
                start_x, start_y = get_position()
                if len(piece) > 3:
                    for i in range(3, len(piece)-1, 2):
                        move(x+float(piece[i])*scale_rate, y+float(piece[i+1])*scale_rate, absolute=True, duration=LINE_DURATION)
            
            case "m": #Move to point (relative)
                release(button="left")
                move(float(piece[-2])*scale_rate, float(piece[-1])*scale_rate, absolute=False, duration=0) 
                press(button="left")
                start_x, start_y = get_position()
                if len(piece) > 3:
                    for i in range(3, len(piece)-1, 2):
                        move(float(piece[i])*scale_rate, float(piece[i+1])*scale_rate, absolute=False, duration=LINE_DURATION)
            
            case "L": #Line to point (absolute)
                for i in range(1, len(piece)-1, 2): # -1 -> if there is an addinational number
                    move(x+float(piece[i])*scale_rate, y+float(piece[i+1])*scale_rate, absolute=True, duration=LINE_DURATION)
            
            case "l": #Line to point (relative)
                for i in range(1, len(piece)-1, 2): # -1 -> if there is an addinational number
                    move(float(piece[i])*scale_rate, float(piece[i+1])*scale_rate, absolute=False, duration=LINE_DURATION)
            
            case "H": #Horizontal line to point (absolute)
                for i in range(1, len(piece)):
                    move(x+float(piece[i])*scale_rate, current_y, absolute=True, duration=LINE_DURATION)
            
            case "h": #Horizontal line to point (relative)
                for i in range(1, len(piece)):
                    move(float(piece[i])*scale_rate, 0, absolute=False, duration=LINE_DURATION)
            
            case "V": #Vertical line to point (absolute)
                for i in range(1, len(piece)):
                    move(current_x, y+float(piece[i])*scale_rate, absolute=True, duration=LINE_DURATION)
            
            case "v": #Vertical line to point (relative)
                for i in range(1, len(piece)):
                    move(0, float(piece[i])*scale_rate, absolute=False, duration=LINE_DURATION)

            case "C": #Cubic bézier (absolute)
                for i in range(1, len(piece)-5, 6): #step is 6 -> 6 coordinates
                    dx1, dy1, dx2, dy2, dx, dy = [float(coord)*scale_rate for coord in piece[i:i+6]] #absolute points
                    __draw_cubic_bezier(current_x, current_y, x+dx1, y+dy1, x+dx2, y+dy2, x+dx, y+dy)
                    mirror_x = 2*dx - dx2 + x if dx != dx2 else dx+x #for Cubic bézier S-s command
                    mirror_y = 2*dy - dy2 + y if dy != dy2 else dy+y #for Cubic bézier S-s command
                    current_x, current_y = x+dx, y+dy #for multiple Cubic bézier
            
            case "c": #Cubic bézier (relative)
                for i in range(1, len(piece)-5, 6):  #step is 6 -> 6 coordinates
                    dx1, dy1, dx2, dy2, dx, dy = [float(coord)*scale_rate for coord in piece[i:i+6]] #relative points
                    __draw_cubic_bezier(current_x, current_y, current_x+dx1, current_y+dy1, current_x+dx2, current_y+dy2, current_x+dx, current_y+dy)
                    mirror_x = 2*dx - dx2 + current_x #for Cubic bézier S-s command
                    mirror_y = 2*dy - dy2 + current_y #for Cubic bézier S-s command
                    current_x, current_y = current_x+dx, current_y+dy #for multiple Cubic bézier
            
            case "Q": #Quadratic bézier (absolute)
                for i in range(1, len(piece)-3, 4):
                    dx1, dy1, dx, dy = [float(coord)*scale_rate for coord in piece[i:i+4]] #absolute points
                    __draw_quadratic_bezier(current_x, current_y, x+dx1, y+dy1, x+dx, y+dy)
                    current_x, current_y = x+dx, y+dy #for multiple Quadratic bézier
            
            case "q": #Quadratic bézier (relative)
                for i in range(1, len(piece)-3, 4):
                    dx1, dy1, dx, dy = [float(coord)*scale_rate for coord in piece[i:i+4]] #relative points
                    __draw_quadratic_bezier(current_x, current_y, current_x+dx1, current_y+dy1, current_x+dx, current_y+dy)
                    current_x, current_y = current_x+dx, current_y+dy #for multiple Quadratic bézier

            case "S": #Smooth to (absolute)
                for i in range(1, len(piece)-3, 4):
                    dx2, dy2, dx, dy = [float(coord)*scale_rate for coord in piece[i:i+4]]
                    __draw_cubic_bezier(current_x, current_y, mirror_x, mirror_y, x+dx2, y+dy2, x+dx, y+dy)
                    mirror_x = 2*dx - dx2 + x if dx != dx2 else dx+x #for Cubic bézier S-s command
                    mirror_y = 2*dy - dy2 + y if dy != dy2 else dy+y #for Cubic bézier S-s command
                    current_x, current_y = x+dx, y+dy #for multiple Cubic bézier s commands

            case "s":
                for i in range(1, len(piece)-3, 4):
                    dx2, dy2, dx, dy = [float(coord)*scale_rate for coord in piece[i:i+4]]
                    __draw_cubic_bezier(current_x, current_y, mirror_x, mirror_y, current_x+dx2, current_y+dy2, current_x+dx, current_y+dy)
                    mirror_x = 2*dx - dx2 + current_x #for Cubic bézier S-s command
                    mirror_y = 2*dy - dy2 + current_y #for Cubic bézier S-s command
                    current_x, current_y = current_x+dx, current_y+dy #for multiple Cubic bézier s commands

            case "T":
                pass

            case "t":
                pass

            case "Z" | "z": #Go to start point
                move(start_x, start_y, absolute=True, duration=LINE_DURATION)
                release(button="left")
        sleep(0.01)
        current_x, current_y = get_position()
    release(button="left")
