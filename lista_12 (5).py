
meters = int(input("Na jakiej wysokości lecimi w metrach?:"))

def height(meters):
    height = meters / 1000
    if height < 5:
       print("Za nisko")
    else:
       print("Jest git")
    return 345678

height(meters)