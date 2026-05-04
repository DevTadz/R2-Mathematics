# Adding f.ex A<1, 3> with B<3, 4>


def main():
    vector_a_str = input("Write vector 1 in format <x,y>: ") #
    vector_b_str = input("Write vector 2 in format <x,y>: ")

    vector_a_components = vector_a_str.replace(" ", "").removeprefix("<").removesuffix(">").split(",")
    vector_b_components = vector_b_str.replace(" ", "").removeprefix("<").removesuffix(">").split(",")

    vector_c_x = int(vector_a_components[0]) + int(vector_b_components[0])
    vector_c_y = int(vector_a_components[1]) + int(vector_b_components[1])

    print(f"Vector {vector_a_str} + {vector_b_str} = <{vector_c_x}, {vector_c_y}>")

main()