import math

def derivative_of_func(f, x, h=1e-5): # h = Δx
    return (f(x + h) - f(x))/h

def f(x):
    return x **2

def g(x):
    return math.sin(x)

evaluation = [-2, -1, 0, 1, 2]

for i in range(len(evaluation)):
    x = evaluation[i]
    print(f"x: {x}", f"| f(x): {f(x)}", f"| f'(x): {round(derivative_of_func(f, x))}")

print(" ")
print("- - - - - - - - - - -")
print(" ")

for i in range(len(evaluation)):
    x = evaluation[i]
    print(f"x: {x}", f"| g(x): {round(g(x), 2)}", f"| g'(x): {round(derivative_of_func(g, x), 2)}")