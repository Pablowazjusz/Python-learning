class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def make_sound(self):
        pass

    def description(self):
        print("Jestem", self.name, "i mam", self.age, "lat.")


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print("Miau!")

    def description(self):
        super().description()
        print("Jestem kotem o kolorze", self.color)


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def make_sound(self):
        print("Hau!")

    def description(self):
        super().description()
        print("Jestem psem rasy", self.breed)


class Bird(Animal):
    def __init__(self, name, age, species):
        super().__init__(name, age)
        self.species = species

    def make_sound(self):
        print("Ćwir, ćwir!")

    def description(self):
        super().description()
        print("Jestem ptakiem gatunku", self.species)


class Fish(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def make_sound(self):
        print("...")

    def description(self):
        super().description()
        print("Jestem rybą o kolorze", self.color)


kot = Cat("Mruczek", 3, "czarny")
kot.make_sound()
kot.description()

pies = Dog("Burek", 5, "owczarek niemiecki")
pies.make_sound()
pies.description()

ptak = Bird("Paweł", 2, "kanarek")
ptak.make_sound()
ptak.description()

ryba = Fish("Nemo", 1, "pomarańczowy")
ryba.make_sound()
ryba.description()
