# python calculator

operator = input("enter operator: ")

num1 = float(input("first number: "))
num2 = float(input("second number: "))

result = ""
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result =  num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    result = num1 / num2
else: 
    print(f"{operator} is not a valid oprator")
        
print (result)
