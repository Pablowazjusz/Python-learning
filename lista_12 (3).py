import math
def ball(r):
    Pb = 4 * math.pi * r ** 2
    Vb = 4/3 * math.pi * r ** 3
    return Pb, Vb

def cone(r, l, h):
    Pc = math.pi * r * (r + l)
    Vc = math.pi * r^2 * h / 3
    return Pc, Vc

def cube(a):
    Pcu = 6 * a^2
    Vcu = a^3
    return Pcu, Vcu

