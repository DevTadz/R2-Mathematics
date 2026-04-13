from enum import Enum
import math

class Triangle:
    def __init__(self, hyp, opp, adj):
        self.hyp = hyp
        self.opp = opp
        self.adj = adj

class TriangleSide(Enum):
    Opposite = 1
    Adjacent = 2
    Hypotenus = 3

def main():
    # Define what areas of triangle is known
    print("1: Opposite")
    print("2: Adjacent")
    print("3: Hypotenus")
    knownSidesAsStr = input("Define 2 known sides seperated with ',': ").replace(" ", "")
    knownSides = knownSidesAsStr.split(",")

    # Add known triangle side values
    triangle = Triangle(0, 0, 0)

    for i in range(len(knownSides)):
        triangleSide = TriangleSide(int(knownSides[i]))
        typeValueAsStr = input(f"{triangleSide.name}: ")

        if(int(knownSides[i]) == TriangleSide.Opposite.value):
            triangle.opp = int(typeValueAsStr)
        elif(int(knownSides[i]) == TriangleSide.Adjacent.value):
            triangle.adj = int(typeValueAsStr)
        elif(int(knownSides[i]) == TriangleSide.Hypotenus.value):
            triangle.hyp = int(typeValueAsStr)

    triangle = find_missing_side(triangle)
    print(calculate_sin(triangle))
    print(calculate_cos(triangle))
    print(calculate_tan(triangle))

def find_missing_side(triangle: Triangle):
    if(triangle.hyp == 0):
        triangle.hyp = math.sqrt(triangle.adj ** 2 + triangle.opp ** 2)
    elif(triangle.opp == 0):
        triangle.opp = math.sqrt(triangle.hyp ** 2 - triangle.adj ** 2)
    elif(triangle.adj == 0):
        triangle.adj = math.sqrt(triangle.hyp ** 2 - triangle.opp ** 2)

    return triangle

def calculate_sin(triangle: Triangle):
    # SOH
    return f"Sin = {str(triangle.opp)}/{str(triangle.hyp)}, decimal value: {str(triangle.opp / triangle.hyp)}"

def calculate_cos(triangle: Triangle):
    # CAH
    return f"Cos = {str(triangle.adj)}/{str(triangle.hyp)}, decimal value: {str(triangle.adj / triangle.hyp)}"

def calculate_tan(triangle: Triangle):
    # TOA
    return f"Tan = {str(triangle.opp)}/{str(triangle.adj)}, decimal value: {str(triangle.opp / triangle.adj)}"
        
main()