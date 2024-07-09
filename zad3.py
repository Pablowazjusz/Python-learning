class Citizen:
    def __init__(self):
        self.first_name = ""
        self.last_name = ""
        self.street = ""
        self.house_number = ""
        self.postal_code = ""
        self.city = ""

    def input_data(self):
        self.first_name = input("Podaj imię: ")
        self.last_name = input("Podaj nazwisko: ")
        self.street = input("Podaj nazwę ulicy: ")
        self.house_number = input("Podaj numer domu: ")
        self.postal_code = input("Podaj kod pocztowy: ")
        self.city = input("Podaj miasto: ")

    def display(self):
        print("----------------------")
        print(f"{self.first_name} {self.last_name}")
        print(f"{self.street} {self.house_number}")
        print(f"{self.postal_code} {self.city}")
        print("----------------------")

    def save_to_file(self, file_name):
        with open(file_name, "w") as file:
            file.write("----------------------\n")
            file.write(f"{self.first_name} {self.last_name}\n")
            file.write(f"{self.street} {self.house_number}\n")
            file.write(f"{self.postal_code} {self.city}\n")
            file.write("----------------------\n")


citizen = Citizen()

citizen.input_data()

citizen.display()

citizen.save_to_file("business_card.txt")
