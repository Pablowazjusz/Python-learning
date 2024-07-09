
class Smartphone:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def year(self, year):
        return "{} jest z {}".format(self.model, year)

    def price(self, price):
        return "Aktualna cena wynosi {}".format(price)

samsung = Smartphone("Samsung", "Galaxy S23")

print("{} {}".format(samsung.brand, samsung.model))
print("{}".format(samsung.year(2023)))
print("{}".format(samsung.price("4149zł")))