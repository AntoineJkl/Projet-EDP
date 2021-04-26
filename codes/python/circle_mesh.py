filename = "cylinder"

# Modules import
import gmsh
import sys
import math
import os
from convertmesh import convert2D

# ------------------------------- Init GMSH
gmsh.initialize(sys.argv)
model = gmsh.model
model.add("OseenCylinder")

# ------------------------------- Parameters
# Border parameters
xlim = [-2, 6]
ylim = [-3, 3]
h_b = 0.1 # Mesh size on border

# Circle parameters
center = [0, 0]
radius = .5
h_c = 0.1 # Mesh size on circle

# ------------------------------- Create points
points = [] # tags of the points 
# border points
points.append(model.geo.addPoint(xlim[0], ylim[0], 0, h_b))
points.append(model.geo.addPoint(xlim[1], ylim[0], 0, h_b))
points.append(model.geo.addPoint(xlim[1], ylim[1], 0, h_b))
points.append(model.geo.addPoint(xlim[0], ylim[1], 0, h_b))

# circle points
points.append(model.geo.addPoint(center[0]-radius, center[1], 0, h_c))
points.append(model.geo.addPoint(center[0],        center[1], 0, h_c))
points.append(model.geo.addPoint(center[0]+radius, center[1], 0, h_c))

# ------------------------------- Create lines
lines = [] # tags of the lines
# border lines
lines.append(model.geo.addLine(1, 2))
lines.append(model.geo.addLine(2, 3))
lines.append(model.geo.addLine(3, 4))
lines.append(model.geo.addLine(4, 1))

# circle lines
lines.append(model.geo.addCircleArc(5, 6, 7))
lines.append(model.geo.addCircleArc(7, 6, 5))

# ------------------------------- Create CurveLoop
border = model.geo.addCurveLoop(lines[:4])
circle = model.geo.addCurveLoop(lines[4:])

# ------------------------------- Create Surface
surf = model.geo.addPlaneSurface([border, circle])

# ------------------------------- Create Physical groups
model.addPhysicalGroup(1, lines[1:4:2], 1) # L-R borders
model.addPhysicalGroup(1, lines[0:3:2], 2) # U-P borders
model.addPhysicalGroup(1, lines[4:], 3) # circle borders

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