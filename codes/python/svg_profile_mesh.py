filename = "wing_propeller"

# Modules import
import svgpathtools
import xml.dom.minidom  
import gmsh
import sys
import os
from convertmesh import convert2D

# Gmsh model build
gmsh.initialize(sys.argv)
model = gmsh.model
model.add(filename)
h_border = .5    # Mesh size of the border
h_curve = 1   # Mesh size of the curve

# ------------------------------- BORDER BUILD 
xlim = [-2, 6]
ylim = [-3, 3]

points_b = [] # tags of border points 
points_b.append(model.geo.addPoint(xlim[0], ylim[0], 0, h_border))
points_b.append(model.geo.addPoint(xlim[1], ylim[0], 0, h_border))
points_b.append(model.geo.addPoint(xlim[1], ylim[1], 0, h_border))
points_b.append(model.geo.addPoint(xlim[0], ylim[1], 0, h_border))

lines_b = [] # tags of border lines
lines_b.append(model.geo.addLine(points_b[0], points_b[1]))
lines_b.append(model.geo.addLine(points_b[1], points_b[2]))
lines_b.append(model.geo.addLine(points_b[2], points_b[3]))
lines_b.append(model.geo.addLine(points_b[3], points_b[0]))

border = model.geo.addCurveLoop(lines_b)

model.addPhysicalGroup(1, lines_b[1:4:2], 1)
model.addPhysicalGroup(1, lines_b[0:3:2], 2)

# ------------------------------- CURVE BUILD
r_factor = [1/100, -1/100] # (x,y) resizing factor (+ vertical flipping)
t_factor = [0, 0] # (x,y) translation factor

# .svg file reading
mydoc = xml.dom.minidom.parse("profils/" + filename + ".svg")
path_tag = mydoc.getElementsByTagName("path")
d_string = path_tag[0].attributes['d'].value
Path_elements = svgpathtools.parse_path(d_string)

# Convert to cartesian coordinates + add points
points = []
for line in Path_elements :
    points.append(line.start)
    points.append(line.control1)
    points.append(line.control2)

points_c = [] # tags of curve points
for p in points:
    points_c.append(
        model.geo.addPoint(
            p.real * r_factor[0] + t_factor[0],
            p.imag * r_factor[1] + t_factor[1],
            0, h_curve)
        )

points_c.append(points_c[0]) # close the loop

lines_c = [] # tags of curve lines
for i in [j for j in range(len(points)) if j%3 ==0]:
    lines_c.append(model.geo.addBSpline(points_c[i:i+4]))

curve = model.geo.addCurveLoop(lines_c)

model.addPhysicalGroup(1, lines_c, 3)

# ------------------------------- SURFACE BUILD
surf = model.geo.addPlaneSurface([border, curve])
model.addPhysicalGroup(2, [surf])

# ------------------------------- MESH BUILD
model.geo.synchronize()
model.mesh.generate(2)

# ------------------------------- EXPORT
gmsh.write("temp.mesh") # .mesh file export

if '-display' in sys.argv: # if display wanted
    gmsh.fltk.run()

gmsh.finalize()

# Converting into 2D-mesh and remove temporary file
convert2D(filename) 
os.remove("temp.mesh")