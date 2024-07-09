class Restaurant:
    def __init__(self, name, cuisine_type):
        self.name = name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print("Restauracja:", self.name)
        print("Rodzaj jedzenia:", self.cuisine_type)

    def open_restaurant(self):
        print("Restauracja jest otwarta.")


class IceCreamStand(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.flavors = []

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def display_flavors(self):
        print("Dostępne smaki lodów:")
        for flavor in self.flavors:
            print("-", flavor)


class CoffeeShop(Restaurant):
    def __init__(self, name, cuisine_type):
        super().__init__(name, cuisine_type)
        self.coffee = []

    def add_coffee(self, coffee_type):
        self.coffee.append(coffee_type)

    def display_coffee(self):
        print("Dostępne rodzaje kawy:")
        for coffee_type in self.coffee:
            print("-", coffee_type)



ice_cream_stand = IceCreamStand("Dobre Lody", "Lody")
ice_cream_stand.add_flavor("Waniliowe")
ice_cream_stand.add_flavor("Czekoladowe")
ice_cream_stand.add_flavor("Truskawkowe")
ice_cream_stand.display_flavors()
ice_cream_stand.describe_restaurant()
ice_cream_stand.open_restaurant()
print()


coffee_shop = CoffeeShop("Kawowe", "Kawa")
coffee_shop.add_coffee("Americano")
coffee_shop.add_coffee("Latte")
coffee_shop.add_coffee("Cappuccino")
coffee_shop.display_coffee()
coffee_shop.describe_restaurant()
coffee_shop.open_restaurant()
