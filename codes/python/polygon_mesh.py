filename = "pentagon"

# Modules import
import gmsh
import sys
import math
import os
from convertmesh import convert2D

# ------------------------------- Init GMSH
gmsh.initialize(sys.argv)
model = gmsh.model
model.add("OseenPolygon")

# ------------------------------- Parameters
# Border parameters
xlim = [-2, 6]
ylim = [-3, 3]
h_b = .1 # Mesh size on border

# Polygon parameters
center = [0, 0]
nb_sides = 5
radius = math.sqrt(2)/2
rotation = math.pi*0
h_p = .1 # Mesh size on polygon

# ------------------------------- Create points
points = [] # tags of the points 
# border points
points.append(model.geo.addPoint(xlim[0], ylim[0], 0, h_b))
points.append(model.geo.addPoint(xlim[1], ylim[0], 0, h_b))
points.append(model.geo.addPoint(xlim[1], ylim[1], 0, h_b))
points.append(model.geo.addPoint(xlim[0], ylim[1], 0, h_b))

# polygons points
for i in range(nb_sides):
    points.append(model.geo.addPoint(
        center[0] + radius*math.cos(2*math.pi*i/nb_sides - rotation),
        center[1] + radius*math.sin(2*math.pi*i/nb_sides - rotation),
        0, h_p)
    )
    
# ------------------------------- Create lines
lines = [] # tags of the lines
# border lines
lines.append(model.geo.addLine(points[0], points[1]))
lines.append(model.geo.addLine(points[1], points[2]))
lines.append(model.geo.addLine(points[2], points[3]))
lines.append(model.geo.addLine(points[3], points[0]))

# polygons lines
for i in range(nb_sides-1):
    lines.append(model.geo.addLine(points[4+i], points[5+i]))
lines.append(model.geo.addLine(points[nb_sides+3], points[4]))

# ------------------------------- Create CurveLoop
border = model.geo.addCurveLoop(lines[:4])
circle = model.geo.addCurveLoop(lines[4:])

# ------------------------------- Create Surface
surf = model.geo.addPlaneSurface([border, circle])

# ------------------------------- Create Physical groups
model.addPhysicalGroup(1, [lines[0], lines[2], lines[3]], 1) # U-L-D borders
model.addPhysicalGroup(1, [lines[1]], 2) # R borders
model.addPhysicalGroup(1, lines[4:], 3)  # circle borders

model.addPhysicalGroup(2, [surf]) # surface

# ------------------------------- Mesh build
gmsh.model.geo.synchronize()

model.mesh.generate(2) # Mesh(2D)

# ------------------------------- File export
gmsh.write("temp.mesh")

if '-display' in sys.argv: # if display wanted
    gmsh.fltk.run()

gmsh.finalize()

# Converting into 2D-mesh and remove temporary file
convert2D(filename) 
os.remove("temp.mesh")