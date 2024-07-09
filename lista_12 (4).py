feet = int(input("Podaj ilość stóp:"))

def converter(feet):
    cm = feet * 30.48
    m = feet * 0.30
    km = feet * 0.0003
    return cm, m, km
print(converter(feet))