
# a1 = 3

# a(2) = a(1) + d
# a3 = a2 + d
# a4 = a3 + d

a1 = 2

def a(n):
    if(n == 1): # first number sequence
        return a1
    else:
        return 2*a(n - 1)+1

def main():
    programActive = True
    while(programActive):
        try:
            str_input = input("Number of instances or q to quit: ")

            if(str_input == 'q'):
                print("Goodbye!")
                programActive = False
                break

            numberOfInstances = int(str_input) 

            for n in range(1, numberOfInstances + 1):
                print(f"a({n}) = {a(n)}")

        except Exception as e:
            print(f"\033[31m Error: {e} \033[0m") 

main()