# Find the equation for plane based on point and normal vector

# let 𝛼 be a plane in the 3d space, let Q(x0, y0, z0) be a constant point in the plane and vector n = [a,b,c] a normal vector in to the plane

# For point P that is in the plane use the rule: (vector QP)⊥(normal vector) which gives us:
# QP * n = 0
# [x - x0, y - y0, z - z0] * [a, b, c] = 0
# a * (x - x0) + b * (y - y0) + c * (z - z0) = 0

# This equation describes plane 𝛼, alle points (x, y, z) that relates to this equation is a point in the plane.

# To find this equation you then need a point in the plane and a Normal vector

# X0 Y0 Z0
point = [1, 2, 3]
# A B C
normalVector = [2, 3, 4]

def findPlane(point, normalVector):
    a = normalVector[0]
    b = normalVector[1]
    c = normalVector[2]

    x0 = point[0]
    y0 = point[1]
    z0 = point[2]

    equation = f"{a}x + {b}y + {c}z + {-(a * x0) - (b * y0) - (c * z0)}"

    return equation

print(findPlane(point, normalVector))