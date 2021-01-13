import math
def formula(d):
    c = 50
    h = 30
    q = round(math.sqrt((2*c*d) / h))
    return q

print(formula(100))