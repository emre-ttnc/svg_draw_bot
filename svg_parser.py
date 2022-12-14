from xml.dom import minidom


def parse_svg(file_path):
    with open(file_path, "r") as svg_file:
        doc = minidom.parse(svg_file)
    
    if doc:
        file = doc.getElementsByTagName("svg")[0]
        
        # get viewBox attribute to scale drawing
        viewBox = file.getAttribute("viewBox")

        #if viewBox property exists
        if viewBox:
            start_x, start_y, end_x, end_y = list(map(float, viewBox.split()))

        else:
            width = file.getAttribute("width")
            height = file.getAttribute("height")
            start_x, start_y, end_x, end_y = float(0), float(0), float(width), float(height)

        ### ELEMENTS ###
        elements = []

        #get elements
        def get_elements(node, elements = elements):
            if node.nodeType is minidom.Node.ELEMENT_NODE:
                for child in node.childNodes:
                    get_elements(child)
                if node.nodeName in ["rect", "circle", "ellipse", "line", "polygon", "polyline", "path"]:
                    elements.append(node)
        
        get_elements(file)
        
        return start_x, start_y, end_x, end_y, elements
