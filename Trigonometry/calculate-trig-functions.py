from enum import Enum

class TriangleValue:
    def __init__(self, triangleValue, triangleType):
        self.triangleValue = triangleValue
        self.triangleType = triangleType

class TriangleType(Enum):
    Opposite = 1
    Adjacent = 2
    Hypotenus = 3

def main():
    # Define what areas of triangle is known
    print("1: Opposite")
    print("2: Adjacent")
    print("3: Hypotenus")
    typesAsString = input("Define 2 known sides seperated with ',': ").replace(" ", "")
    types = typesAsString.split(",")

    # Add triangle values
    triangleDefinitions = []

    for i in range(len(types)):
        triangleValue = TriangleValue()
        typeValue = input(types[i] + " value: ")
        triangleValue.triangleType = types[i]
        triangleValue.triangleValue = typeValue
        triangleDefinitions.append(triangleValue)

# def calculate_trigonometric_functions(triangleDefinitions):

main()