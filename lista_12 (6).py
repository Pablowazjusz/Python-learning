number = int(input("Podaj zmienną:"))

def Binary(number):
    binary = bin(number)[2:]
    print(binary)

def Hexadecimal(number):
    hexidecimal = hex(number)
    print(hexidecimal)

def Octal(number):
    octal = oct(number)
    print(octal)


Binary(number)
Hexadecimal(number)
Octal(number)