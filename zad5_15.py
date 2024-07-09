class RoomNumber:
    def __init__(self, floor, room):
        self.floor = floor
        self.room = room

    def __repr__(self):
        return f"Floor: {self.floor}, Room: {self.room}"


class Person:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Person: {self.name}"


class Hotel:
    def __init__(self, floors, rooms_per_floor):
        self.floors = floors
        self.rooms_per_floor = rooms_per_floor
        self.rooms = {}
        self.occupied_rooms = {}

        for floor in range(1, floors + 1):
            for room in range(1, rooms_per_floor + 1):
                room_number = RoomNumber(floor, room)
                self.rooms[room_number] = None

    def has_available_room(self):
        return any(room is None for room in self.rooms.values())

    def count_available_rooms(self):
        return sum(room is None for room in self.rooms.values())

    def assign_room_to_person(self, person):
        for room_number, occupant in self.rooms.items():
            if occupant is None:
                self.rooms[room_number] = person
                self.occupied_rooms[person] = room_number
                return room_number
        return None

    def are_adjacent_rooms_available(self):
        for room_number, occupant in self.rooms.items():
            if occupant is None:
                adjacent_room_number = RoomNumber(room_number.floor, room_number.room + 1)
                if adjacent_room_number in self.rooms and self.rooms[adjacent_room_number] is None:
                    return room_number
        return None

    def is_person_renting_room(self, person_name):
        return any(person.name == person_name for person in self.occupied_rooms.keys())

    def get_available_rooms_for_person(self, person_name):
        return [room_number for person, room_number in self.occupied_rooms.items() if person.name == person_name]

    def get_all_rooms_for_person(self, person_name):
        return [room_number for person, room_number in self.occupied_rooms.items() if person.name == person_name]


hotel = Hotel(floors=3, rooms_per_floor=5)

print("Available rooms:", hotel.count_available_rooms())

john = Person("John")

room_assigned = hotel.assign_room_to_person(john)
print(room_assigned)

john_rooms_available = hotel.get_available_rooms_for_person("John")
print("Johns room" ,john_rooms_available)