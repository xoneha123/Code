from random import *
color_list = ["red", "orange", "yellow", "green", "blue", "purple"]
choice = input("type 2 or 3 to choose how many colors your team will have: ")

if choice == "2":
    color1 = color_list[randrange(len(color_list))]
    color2 = color_list[randrange(len(color_list))]
    print("you team colors are " + color1 + " and " + color2 + ".")
elif choice == "3":
    color1 = color_list[randrange(len(color_list))]
    color2 = color_list[randrange(len(color_list))]
    color3 = color_list[randrange(len(color_list))]
    print("you team colors are " + color1 + " and " + color2 + " and " + color3)
else:
    print("you cn only pick 2 or 3.")
