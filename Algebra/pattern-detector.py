def is_sequence_arithmetic(number_sequence):
    list_of_diffs = []

    for i in range(len(number_sequence)):
        if(i + 1 != len(number_sequence)):
            diff = number_sequence[i] - number_sequence[i + 1]
            if(diff not in list_of_diffs):
                list_of_diffs.append(diff)

    return len(list_of_diffs) == 1

def is_sequence_geometric(number_sequence):
    list_of_ratios = []

    for i in range(len(number_sequence)):
        if(i + 1 != len(number_sequence)):
            ratio = number_sequence[i] / number_sequence[i + 1]
            if(ratio not in list_of_ratios):
                list_of_ratios.append(ratio)

    return len(list_of_ratios) == 1

def geometric_pattern(number_sequence): 
    n = 1
    a1 = number_sequence[0]
    an = number_sequence[n]
    r = (an/a1) # using number_sequence[1] just to test 6/2 = 3. ([2, 6, 18, 54])
 
    return f"a(n) = {a1} * {int(r)}^n-1"

def arithmetic_pattern(number_sequence):
    a1 = number_sequence[0]
    common_difference = number_sequence[1] - number_sequence[0] # a2 - a1

    return f"a(n) = {a1} + {common_difference}n - {common_difference}"


def main():
    programActive = True
    #number_sequence = [2, 4, 6, 8] 
    #number_sequence = [2, 6, 18, 54]
    #number_sequence = [4, 7, 10, 13, 16]

    while(programActive):
        try:
            print("\033[1;32m--- WRITE q to QUIT ---\033[0m")
            str_input = input("Write sequence with , between: ")
            print(" ")

            if(str_input == "q"):
                print("Goodbye!")
                programActive = False
                break

            number_sequence_str = str_input.strip().split(",")
            number_sequence = [int(x) for x in number_sequence_str]

            if(len(number_sequence) == 1):
                raise Exception("List needs to be longer than 1")

            if(is_sequence_arithmetic(number_sequence)):
                print(f"Pattern: {arithmetic_pattern(number_sequence)}. (Arithmetic)")
            elif(is_sequence_geometric(number_sequence)):
                print(f"Pattern: {geometric_pattern(number_sequence)}. (Geometric)")
            else:
                print("couldnt detect :(")
            print(" ")

        except Exception as e:
            print(f"\033[31m Error: {e} \033[0m") 
            print(" ")


main()