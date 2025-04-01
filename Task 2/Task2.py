
import math, sys

#circle_file = input("Введите путь файла круга: ")
#dot_file = input("Введите путь файла точек: ")
#circle_file = "C:/Users/Riht/Desktop/Job/Performance Labs/Task 2/circle.txt"
#dot_file = "C:/Users/Riht/Desktop/Job/Performance Labs/Task 2/dot.txt"

circle_file = sys.argv[1]
dot_file = sys.argv[2]

with open(circle_file) as file:
    lines = [line.rstrip() for line in file]
    circle_center1, circle_center2 = lines[0].split(" ")
    circle_radius = int(lines[1])

with open(dot_file) as file:
    for line in file:
        first_coordinate, second_coordinate = line.split(" ")
        #sqrt((X - xc) ** 2 + (Y - yc) ** 2)
        equation = math.sqrt((int(first_coordinate) - int(circle_center1)) ** 2 + (int(second_coordinate) - int(circle_center2)) ** 2)
        if equation == int(circle_radius):
            print("0")
        elif equation < int(circle_radius):
            print("1")
        else:
            print("2")

