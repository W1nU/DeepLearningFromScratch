import AND
import NAND_OR
 
def XOR(x1, x2):
    s1 = NAND_OR.NAND(x1, x2)
    s2 = NAND_OR.OR(x1, x2)
    y = AND.AND(s1, s2)

    return y

print(XOR(0,0)) # 0
print(XOR(1,0)) # 1
print(XOR(0,1)) # 1
print(XOR(1,1)) # 0