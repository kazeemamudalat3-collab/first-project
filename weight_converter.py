# weight converter

weight = float(input("Enter weight: "))
unit = input("weight units: K or L: ").upper()

if unit  == "K":
    weight = weight*2.025
    unit = "lbs."
    print (f"your weight is {round(weight, 1)} {unit}")

elif unit == "L":
    weight = weight/2.025
    unit = "kgs."
    print (f"your weight is {round(weight, 1)} {unit}")
else:
    print(f"{unit} is invalid unit inputted")

