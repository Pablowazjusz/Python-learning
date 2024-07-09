class Beer:
    def __init__(self, name, category, concentration, price):
        self.name = name
        self.category = category
        self.concentration = concentration
        self.price = price
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def average_rating(self):
        if not self.reviews:
            return 0

        total_ratings = sum(self.reviews)
        return total_ratings / len(self.reviews)

    def __str__(self):
        return f"Beer: {self.name}, Category: {self.category}, Concentration: {self.concentration}%, Price: {self.price}"


class Shop:
    def __init__(self, name):
        self.name = name
        self.beers = []

    def add_beer(self, beer):
        self.beers.append(beer)

    def sort_by_rating(self):
        self.beers.sort(key=lambda x: x.average_rating(), reverse=True)

    def sort_by_name(self):
        self.beers.sort(key=lambda x: x.name)

    def __str__(self):
        return f"Sklep: {self.name}"



shop = Shop("BeerStore")

beer1 = Beer("IPA", "India Pale Ale", 6.5, 10.99)
beer1.add_review(4)
beer1.add_review(5)
beer1.add_review(4)
shop.add_beer(beer1)

beer2 = Beer("Stout", "Stout", 7.0, 12.99)
beer2.add_review(5)
beer2.add_review(5)
beer2.add_review(4)
shop.add_beer(beer2)

beer3 = Beer("Lager", "Lager", 4.5, 8.99)
beer3.add_review(3)
beer3.add_review(4)
beer3.add_review(3)
shop.add_beer(beer3)

shop.sort_by_rating()
for beer in shop.beers:
    print(beer)

shop.sort_by_name()
for beer in shop.beers:
    print(beer)
