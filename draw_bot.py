from sys import exit
from select_file import get_file_path
from get_area import get_positions
from svg_parser import parse_svg
from draw_shapes import draw_line, draw_rect, draw_polygon, draw_polyline, draw_circle, draw_ellipse, draw_path
from time import sleep
from re import split


#Get selected area coordinates
start_x, start_y, end_x, end_y = get_positions()

#if it is not an area then close the program
if start_x == end_x or start_y == end_y:
    exit()

#normalize coordinates if selected from the opposite direction
if start_x > end_x:
    start_x, end_x = end_x, start_x
if start_y > end_y:
    start_y, end_y = end_y, start_y

file_path = get_file_path()

#if get_file_path function did not returned any data then close the program
if file_path is None:
    exit()

#get viewBox or width-height attribute and get elements
viewBox_start_x, viewBox_start_y, viewBox_end_x, viewBox_end_y, elements = parse_svg(file_path)
#If these attributes are not set, close the program 
if viewBox_start_x is None or viewBox_start_y is None or viewBox_end_x is None or viewBox_end_y is None or elements is None:
    exit()
drawing_width, drawing_height = (viewBox_end_x - viewBox_start_x), (viewBox_end_y - viewBox_start_y)

#calculate scale and find optimum scale ratio
scale_x = (end_x - start_x) / drawing_width
scale_y = (end_y - start_y) / drawing_height
scale_rate = scale_x if scale_x < scale_y else scale_y

#align the drawing to the center of the area
if scale_x > scale_y:
    start_x += int(((end_x - start_x) - drawing_width * scale_rate) / 2)
elif scale_y > scale_x:
    start_y += int(((end_y - start_y) - drawing_height * scale_rate) / 2)


### GET ATTRIBUTES AND CALL FUNCTIONS ###
def _draw_line(element):
    x1, y1, x2, y2 = element.getAttribute("x1"), element.getAttribute("y1"), element.getAttribute("x2"), element.getAttribute("y2")
    draw_line(
        x1 = start_x+float(x1)*scale_rate, 
        y1 = start_y+float(y1)*scale_rate, 
        x2 = start_x+float(x2)*scale_rate, 
        y2 = start_y+float(y2)*scale_rate)

def _draw_rect(element):
    x, y, width, height = element.getAttribute("x"), element.getAttribute("y"), element.getAttribute("width"), element.getAttribute("height")
    draw_rect(
    x = start_x+float(x)*scale_rate, 
    y = start_y+float(y)*scale_rate, 
    width = float(width)*scale_rate, 
    height = float(height)*scale_rate)

def _draw_polyline(element):
    points = element.getAttribute("points")
    points = split(" |,", points) #seperate points (space and comma)
    draw_polyline(
        x = start_x, 
        y = start_y, 
        scale_rate = scale_rate, 
        points = points)

def _draw_polygon(element): #TODO add Z/z !!
    points = element.getAttribute("points")
    points = split(" |,", points) #seperate points (space and comma)
    draw_polygon(
        x = start_x, 
        y = start_y, 
        scale_rate = scale_rate, 
        points = points)

def _draw_circle(element): ### cx, cy = center x, center y ### r = radius ###
    cx, cy, r = element.getAttribute("cx"), element.getAttribute("cy"), element.getAttribute("r")
    draw_circle(
        cx = start_x + float(cx) * scale_rate,
        cy = start_y + float(cy) * scale_rate,
        r = float(r) * scale_rate)

def _draw_ellipse(element): ### cx, cy = center x, center y ### rx, ry = radius x, radius y ###
    cx, cy, rx, ry = element.getAttribute("cx"), element.getAttribute("cy"), element.getAttribute("rx"), element.getAttribute("ry")
    draw_ellipse(
        cx = start_x + float(cx) * scale_rate,
        cy = start_y + float(cy) * scale_rate,
        rx = float(rx) * scale_rate,
        ry = float(ry) * scale_rate)

def _draw_path(element):
    d = element.getAttribute("d")
    draw_path(d)

sleep(1) #TEST

### CALL FUNCTION FOR EACH ELEMENT ###
for element in elements:
    match element.nodeName:
        case "rect":
            _draw_rect(element)
            continue
        case "ellipse":
            _draw_ellipse(element)
            continue
        case "circle":
            _draw_circle(element)
            continue
        case "line":
            _draw_line(element)
            continue
        case "polygon":
            _draw_polygon(element)
            continue
        case "polyline":
            _draw_polyline(element)
            continue
        case "path":
            _draw_path(element)
            continue