kg = int(input("Podzaj swoją masę:"))
m = float(input("Podaj wzrosy w metrach:"))

def bmi(kg, m):
    BMI = kg / (m * m)
    if BMI < 18.5:
        print("Jesteś zbyt chudy, jedz więcej fast foodów")
    elif BMI > 25:
        print("Jesteś za niski do tej wagi")
    else:
        print("Jesteś git ziomek")



bmi(kg, m)



