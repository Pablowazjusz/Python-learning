# class Parrot:
#     species = "ptak"
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# blu = Parrot("Blu", 10)
# ara = Parrot("Ara", 15)
#
# print("Blu jest{}".format(blu.__class__.species))
# print("Ara jest{}".format(ara.__class__.species))
# print("{}ma{}lat".format( blu.name, blu.age))
# print("{}ma{}lat".format(ara.name,ara.age))

class Car:
    transport = "car"
    def __init__(self, brand, model, type, mileage, color):
        self.brand = brand
        self.model = model
        self.type = type
        self.mileage = mileage
        self.color = color

    def go(self, speed):
        return "{} {} jedzie {}".format(self.brand, self.model, speed)
    def stop(self):
        return "{} zatrzymuje się.".format(self.type)

ferrari = Car("Ferrari", "488", "kabriolet", "60000km", "czerwony" )
toyota = Car("Toyota", "Yaris", "osobówka", "100000000km", "pudrowy róż")




print("Samochód to: marka: {}, model: {}, typ: {}, przebieg: {}, kolor: {}".format(ferrari.brand, ferrari.model, ferrari.type, ferrari.mileage, ferrari.color))
print("Samochód to: marka: {}, model: {}, typ: {}, przebieg: {}, kolor: {}".format(toyota.brand, toyota.model, toyota.type, toyota.mileage, toyota.color))
print(ferrari.go("100km/h"))
print(toyota.stop())