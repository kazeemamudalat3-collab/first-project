# weight converter

weight = float(input("Enter weight: "))
unit = input("weight units: K or L: ").upper()

if unit  == "K":
    weight = weight*2.025
    unit = "lbs."

elif unit == "L":
    weight = weight/2.025
    unit = "kgs."
else:
    print(f"{unit} invalid uint inputted")

print (f"your weight is {round(weight, 1)} {unit}")