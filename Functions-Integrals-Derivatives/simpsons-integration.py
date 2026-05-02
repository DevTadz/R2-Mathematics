import math

def g(x):
    return math.sin(x)

def f(x):
    return x**3

def integrate_simpson(f, a, b, n=1000):
    delta_x = (b-a)/n

    y_i_values = []

    for i in range(n + 1):
        y_i = f(a + (i*delta_x))
        y_i_values.append(y_i)

    #Simpsons Y Pattern 1,4,2,4,2,...,4,1.
    y_calculated_total = 0

    for i in range(len(y_i_values)):
        if(i == 0 or i == (len(y_i_values) - 1)):
            y_calculated_total += y_i_values[i]
        else:
            isEven = i % 2 == 0

            if(isEven):
                y_calculated_total += (2 * y_i_values[i])
            else:
                y_calculated_total += (4 * y_i_values[i])

    return (delta_x/3)*y_calculated_total


print(integrate_simpson(f, 0, 2))
print(integrate_simpson(g, 0, math.pi))