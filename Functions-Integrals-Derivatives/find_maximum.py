def derivative_of_func(f, x, h=1e-5): # h = Δx
    return (f(x + h) - f(x))/h

def f(x):
    return -(x**2)+(4*x)+1

def find_max(f, start=-10, end=10, step=0.001):
    x = start
    
    prev_derivative = derivative_of_func(f, x)
    
    while x <= end:
        x += step
        curr_derivative = derivative_of_func(f, x)
        
        if prev_derivative > 0 and curr_derivative < 0: # Checks for sign change
            return x
        
        prev_derivative = curr_derivative

max_x = find_max(f)
print("Max x ≈", max_x)
print("Max value ≈", f(max_x))

find_max(f)