import numpy as np

def NAND(x1, x2):
    x = np.array([x1, x2])
    w = np.array([-0.5, -0.5]) # AND와는 가중치 w와 b만 다르다
    b = 0.7

    temp = np.sum(w * x) + b

    if temp <= 0:
        return 0
    
    else:
        return 1


def OR(x1, x2):
    x = np.array([x1, x2])
    w = np.array([0.5, 0.5]) # AND와는 가중치 w와 b만 다르다
    b = -0.2

    temp = np.sum(x * w) + b

    if temp <= 0:
        return 0
    
    else:
        return 1
