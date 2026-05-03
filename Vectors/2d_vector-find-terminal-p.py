# Finds terminal point based on Vector properties and point A

def main():
    init_point_str = input("Type initial point as form '(x1, y1)': ") # (-1, -3)
    vector_props_str = input("Type Vector props as form (3i (+ or -) 2j): ") # 3i - 2j

    vector_props = vector_props_str.split(" ") # [3i, -, 2j]

    i = int(vector_props[0].replace("i", "")) # 3 || -3
    j = int(vector_props[1] + vector_props[2].replace("j", "")) # 2 || -2


    init_point_props = init_point_str.removeprefix("(").removesuffix(")").replace(" ", "").split(",")
    x1 = int(init_point_props[0])
    y1 = int(init_point_props[1])

    terminal_point = f"({x1 + i}, {y1 + j})"
    print(terminal_point)

main()





