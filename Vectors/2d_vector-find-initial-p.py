# Finds inital point based on Vector properties and terminal point B

def main():
    terminal_point_str = input("Type terminal point as form '(x2, y2)': ") # (-1, -3)
    vector_props_str = input("Type Vector props as form (3i (+ or -) 2j): ") # 3i - 2j

    vector_props = vector_props_str.split(" ") # [3i, -, 2j]

    i = int(vector_props[0].replace("i", "")) # 3
    j = int(vector_props[1] + vector_props[2].replace("j", "")) # -2


    terminal_point_props = terminal_point_str.removeprefix("(").removesuffix(")").replace(" ", "").split(",")
    x2 = int(terminal_point_props[0])
    y2 = int(terminal_point_props[1])

    initial_point = f"({x2 - i}, {y2 - j})"
    print(initial_point)

main()
