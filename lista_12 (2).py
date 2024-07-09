variable1 = input("Podaj pierwszą zmienną:")
variable2 = input("Podaj drugą zmienną:")

def suma(a,b):
    suma = int(variable1) + int(variable2)
    return suma

def minus(a,b):
    minus = int(variable1) - int(variable2)
    return minus

def multiplication(a,b):
    multi = int(variable1) * int(variable2)
    return multi

def devision(a,b):
    devison = int(variable1) / int(variable2)
    return devison


print("suma", suma(variable1, variable2))
print("różnica", minus(variable1, variable2))
print("mnożenie", multiplication(variable1, variable2))
print("dzielenie", devision(variable1, variable2))










