class Student:
    species = "człowiek"
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def study(self):
        return "{} się uczy.".format(self.name)

    def status(self, hired):
        return "Student {} jest {}.".format(self.name, hired)

    def collage(self, collage):
        return "Student jest studentem {}".format(collage)

paulina = Student("Paulina", 19)

print("{} lat {}".format(paulina.name, paulina.age))
print(paulina.study())
print(paulina.status("zatrudniona"))
print(paulina.collage("Uniwersytetu Dolnośląskiego DSW"))
