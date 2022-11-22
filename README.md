# svg_draw_bot :robot:

## Goal:
This program draws svg elements with the mouse 

## Language:
Python **3.11**

### Libraries (modules):
- tkinter
- xml.dom
- mouse [*PyPI Link*](https://pypi.org/project/mouse/)

## Updates:
- [x] Project created :tada:
- [x] Select and read the file.
- [x] Select draw area and get coordinates.
- [x] Read the SVG file and calculate the scale ratio (and align the drawing to the center of the area)
- [x] Get SVG Elements and parse them
- [x] Draw line, polyline, rectangle and polygon
- [x] Draw circle and ellipse
- [x] Parse path
- [ ] Parse each command and draw M, m, L, l, H, h, V, v and Z/z commands

## Test file
<img src="https://raw.githubusercontent.com/emre-ttnc/svg_draw_bot/72480dfea564af636891fd47d4fab5c612e7d55b/test_files/test1.svg" width="auto">

## Result
<img src="https://github.com/emre-ttnc/svg_draw_bot/blob/main/test_files/result.gif?raw=true" width="auto">
