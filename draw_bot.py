from sys import exit
from select_file import get_file_path
from get_area import get_positions
from svg_parser import parse_svg


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

#get viewBox or width-height attribute
viewBox_start_x, viewBox_start_y, viewBox_end_x, viewBox_end_y, elements = parse_svg(file_path)
drawing_width, drawing_heigt = (viewBox_end_x - viewBox_start_x), (viewBox_end_y - viewBox_start_y)

#calculate scale and find optimum scale ratio
scale_x = (end_x - start_x) / drawing_width
scale_y = (end_y - start_y) / drawing_heigt
scale_rate = scale_x if scale_x < scale_y else scale_y

#align the drawing to the center of the area
if scale_x > scale_y:
    start_x += int(((end_x - start_x) - drawing_width * scale_rate) / 2)
elif scale_y > scale_x:
    start_y += int(((end_y - start_y) - drawing_heigt * scale_rate) / 2)

#test
for element in elements:
    match element.nodeName:
        case "rect":
            #TODO
            continue
        case "ellipse":
            #TODO
            continue
        case "circle":
            #TODO
            continue
        case "line":
            #TODO
            continue
        case "polygon":
            #TODO
            continue
        case "polyline":
            #TODO
            continue
        case "path":
            #TODO
            continue