import math

# very simple calc for getting length.
# The formula for vector length is the pythagoran formula. Where length (h) = x^2 + y^2. Imagine a right triangle 

def get_vector_length(v):
    x = v[0]
    y = v[1]

    return math.sqrt(x**2 + y**2)


print(get_vector_length([3, 4]))

