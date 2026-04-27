def f(x):
    return 3*(x**2)-(4*x)+1

evaluation = [-2, -1, 0, 1, 2]

for i in range(len(evaluation)):
    x = evaluation[i]
    print(f"x: {x}", f"| f(x): {f(x)}")