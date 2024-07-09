import random

natural_number = random.randint(1, 100000)
divisor = []
print(natural_number)
for i in range(1, natural_number + 1):
    if natural_number % i == 0:
        divisor.append(i)
print(divisor)