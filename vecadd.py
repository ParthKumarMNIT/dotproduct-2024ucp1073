import numpy as np

a = list(map(float, input("Enter the first vector (space-separated): ").split()))
b = list(map(float, input("Enter the second vector (space-separated): ").split()))

if len(a) != len(b):
    print("Error: Vectors must be of the same length.")
else:
    dot_product = sum(x * y for x, y in zip(a, b))
    print("Dot product:", dot_product)
print("*output using old code*")

print(np.dot(a, b))
print("Hello")
