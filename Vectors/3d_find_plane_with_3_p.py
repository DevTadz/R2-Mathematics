# finding equation based on point A(4, 0, 0) B(2, 3, 0) and C(0, 0, 2)

# We need to first find normal vector for the plane

# Since AB & AC is int the same plane of Vector AB and Vector AC is directional vectors for the lines between-
# -A & B and A & C will Vector AB * Vector AC = normal vector for the plane
import math

point_a = [4, 0, 0] #XYZ
point_b = [2, 3, 0] #XYZ
point_c = [0, 0, 2] #XYZ

vector_ab = [ # Remember since its A -> B we do B - A (Difference)
    point_b[0] - point_a[0], 
    point_b[1] - point_a[1], 
    point_b[2] - point_a[2]
] 

vector_ac = [ # Remember since its A -> C we do C - A (Difference)
    point_c[0] - point_a[0], 
    point_c[1] - point_a[1], 
    point_c[2] - point_a[2]
]

# FINDING THE CROSS PRODUCT:
# | i   j   k |
# |-2   3   0 |    AB  
# |-4   0   2 |    AC    

i_component = (vector_ab[1] * vector_ac[2]) - (vector_ab[2] * vector_ac[1]) # (3 * 2) - (0 * 0) (Ignore x column)
j_component = (vector_ab[0] * vector_ac[2]) - (vector_ab[2] * vector_ac[0]) # (-2 * 2) - (0 * -4) (Ignore y column)
k_component = (vector_ab[0] * vector_ac[1]) - (vector_ab[1] * vector_ac[0]) # (-2 * 0) - (3 * -4) (Ignore z column)
  
common_factor = math.gcd(i_component, j_component, k_component)

normal_vector = (i_component / common_factor, j_component / common_factor, k_component / common_factor)

print(f"AB = {vector_ab}")
print(f"AC = {vector_ac}")
print(f"Normal vector = {normal_vector}")

def findPlane(point, normalVector):
    a = normalVector[0]
    b = normalVector[1]
    c = normalVector[2]

    x0 = point[0]
    y0 = point[1]
    z0 = point[2]

    equation = f"{a}x + {b}y + {c}z + {-(a * x0) - (b * y0) - (c * z0)}"

    return equation

print(findPlane(point_a, normal_vector)) # Can use any point with the normal vector
