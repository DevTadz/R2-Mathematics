

def main():
    initial_point_str = input("Type initial point as (x1, y1, z1): ")
    terminal_point_str = input("Type initial point as (x2, y2, z2): ")

    initial_points = initial_point_str.removeprefix("(").removesuffix(")").replace(" ", "").split(",")
    terminal_points = terminal_point_str.removeprefix("(").removesuffix(")").replace(" ", "").split(",")

    x1 = int(initial_points[0])
    y1 = int(initial_points[1])
    z1 = int(initial_points[2])

    x2 = int(terminal_points[0])
    y2 = int(terminal_points[1])
    z2 = int(terminal_points[2])

    print(f"V = {x2 - x1}i + {y2 - y1}j + {z2 - z1}k")

main()