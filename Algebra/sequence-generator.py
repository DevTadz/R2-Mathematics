def f(n): # Function of the number series
    return 2**n

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
                print(f"F({n}) = {f(n)}")

        except Exception as e:
            print(f"\033[31m Error: {e} \033[0m") 

main()