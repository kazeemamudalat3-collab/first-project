#  Student Grade Manager
# Create a program that:
# Stores student names and scores in a dictionary.
# Calculates each student's average.
# Determines whether they passed or failed.
# Displa.ys the student with the highest score.

students = {
    "John": [70, 80, 65],
    "Mary": [90, 85, 88],
    "David": [45, 60, 50]
}
try:
    name = input("Enter a name: ").title()
    # if name not in students.items():
        # print("Student not found")
        
    scores = students[name]
    average = round(sum(scores)/len(scores), 2)


    # for name, scores in students.items():
    print(f"{name}:{scores}")
    print (f"{name}:{average}")
    if average < 40:
        print("Failed")
    elif average > 40 or average <= 100:
        print("Passed")
except:
    print("Student not found")
