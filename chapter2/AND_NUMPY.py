import numpy as np

x = np.array([0, 1])
w = np.array([0.5, 0.5])
b = -0.7

print(w * x)
print(np.sum(w * x))
print(np.sum(w * x) + b)

def AND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5])
    b = -0.7

    temp = np.sum(x * w ) + b

    if temp <= 0:
        return 0

    else:
        return 1

print(AND(0, 1))