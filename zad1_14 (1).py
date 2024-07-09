class Vehicle:
    def __init__(self, plate):
        self.plate = plate
        print("Tworzenie obiektu Pojazd")

    def __del__(self):
        print("Usuwanie obiektu Pojazd")

    def drive(self):
        print("Pojazd porusza się.")


class Car(Vehicle):
    def __init__(self, plate, mark, model):
        super().__init__(plate)
        self.mark = mark
        self.model = model
        print("Tworzenie obiektu Samochod")

    def __del__(self):
        print("Usuwanie obiektu Samochod")

    def open_door(self):
        print("Otwieranie drzwi samochodu.")


class Motorcycle(Vehicle):
    def __init__(self, plate, mark, model):
        super().__init__(plate)
        self.mark = mark
        self.model = model
        print("Tworzenie obiektu Motocykl")

    def __del__(self):
        print("Usuwanie obiektu Motocykl")

    def ride_on_wheels(self):
        print("Motocykl wykonuje jazdę na kołach.")


car = Car("ABC123", "Toyota", "Corolla")
car.open_door()
car.drive()
print("Numer rejestracyjny samochodu:", car.plate)
print("Marka samochodu:", car.mark)
print("Model samochodu:", car.model)
del car

print()

motorcycle = Motorcycle("XYZ456", "Honda", "CBR500R")
motorcycle.ride_on_wheels()
motorcycle.drive()
print("Numer rejestracyjny motocyklu:", motorcycle.plate)
print("Marka motocyklu:", motorcycle.mark)
print("Model motocyklu:", motorcycle.model)
del motorcycle