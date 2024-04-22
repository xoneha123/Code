weather = "cool"

def shoe_choice(weather):
    weather = input("is it snowy, cool, or hot.")
    if weather == "snowy":
        print("wear your snow boots.")
    elif weather == "cool":
        print("wear your tennes shoes.")
    elif weather == "hot":
        print("wear your sandles.")

print("when it's snowing...")
shoe_choice("snowy")


print("when its hot...")
shoe_choice("hot")


print("when itd cool...")
shoe_choice("cool")
