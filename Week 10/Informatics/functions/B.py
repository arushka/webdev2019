import math
def po(a, b):
    return math.pow(a,b)


line = input().split()
print(po(float(line[0]), int(line[1])))