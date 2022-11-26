# svg_draw_bot :robot:

## Goal:
This program draws svg elements with the mouse 

## Language:
Python **3.11**

### Libraries (modules):
- tkinter (built-in)
- xml.dom (built-in)
- re (built-in)
- math (built-in)
- time (built-in)
- sys (built-in)
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
- [x] Parse each command and draw M, m, L, l, H, h, V, v and Z/z commands
- [x] Draw c (relative) and C(absolute) (cubic bézier) commands
- [x] Draw q (relative) and Q(absolute) (quadratic bézier) commands
- [x] Draw s (relative) and S(absolute) (cubic bézier smooth curve to) commands
- [x] Draw t (relative) and T(absolute) (quadratic bézier smooth curve to) commands
- [ ] Draw a (relative) and A(absolute) (arc) commands

### Follow these links for additional information on Béziers and SVG path commands
 - [*Bézier Curve*](https://en.wikipedia.org/wiki/B%C3%A9zier_curve)
 - [*SVG Paths*](https://developer.mozilla.org/en-US/docs/Web/SVG/Tutorial/Paths)

## Test file
<img src="https://raw.githubusercontent.com/emre-ttnc/svg_draw_bot/72480dfea564af636891fd47d4fab5c612e7d55b/test_files/test1.svg" width="auto">

## Result
<img src="https://github.com/emre-ttnc/svg_draw_bot/blob/main/test_files/result.gif?raw=true" width="auto">
