# using rule u = v / ||v||
import math

def main():
    vector_a_str = input("Write vector 1 in format <x,y>: ") 
    vector_a_components = vector_a_str.replace(" ", "").removeprefix("<").removesuffix(">").split(",")

    vector_a_magnitude = math.floor(math.sqrt((int(vector_a_components[0])**2) + (int(vector_a_components[1])**2)))

    print(f"u = <{vector_a_components[0]}/{vector_a_magnitude}, {vector_a_components[1]}/{vector_a_magnitude}>")

main()