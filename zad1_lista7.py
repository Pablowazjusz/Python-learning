
tuple = ("pierwszy", 5, 9, "loki", 0, "end")

print(len(tuple))
print(id(tuple))

tuple = tuple + (3, "jednakże")

print(len(tuple))
print(id(tuple))

list = list(tuple)
print(list)