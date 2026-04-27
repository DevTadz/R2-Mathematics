# Implementing integration using the trapezoidal rule
# Integral of f(x) inbetween a -> b with n amount of trapexoids
# File contains subOptimal & optimal function

def f(x):
    return x**2

#[SUB OPTIMAL]:
def integrate_subOptimal(f, a, b, n=5):
    delta_x = (b-a)/n
    points = []

    i = a
    while(True):
        point = delta_x * i
        points.append(point)

        if(point == b):
            break

        i+=1

    print("Evaluating:", points)

    first_fx = f(points[0])
    print(f"f({points[0]}) = {first_fx}")

    middle_fxs = 0

    for i in range(1, len(points) - 1):
        x = points[i]
        middle_fxs += 2 * f(x)
        print(f"f({x}) = {middle_fxs}")
    
    last_fx = f(points[len(points) - 1])
    print(f"f({points[len(points) - 1]}) = {last_fx}")

    Tn = (delta_x / 2) * (first_fx + middle_fxs + last_fx)

    print(f"T{n} = {Tn}")

#[OPTIMAL]:
def integrate_optimal(f, a, b, n=1000):
    dx = (b - a) / n
    
    total = f(a) + f(b)
    
    for i in range(1, n):
        x = a + i * dx
        total += 2 * f(x)
    
    return (dx / 2) * total

result = integrate_optimal(f, 0, 2, 1000)
print("Result:", result)