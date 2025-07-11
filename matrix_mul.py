import numpy as np

def run():
    print("✅ Running matrix calculation...")
    a = np.random.rand(2, 2)
    b = np.random.rand(2, 2)
    print("A =", a)
    print("B =", b)
    print("Result =", np.dot(a, b))
