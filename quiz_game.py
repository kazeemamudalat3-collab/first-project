# Create a dictionary containing questions and answers
# Ask each question and calculate the user's score.
questions = {
    "What is the capital of Nigeria?": "Abuja",
    "What language are you learning?": "Python"
}

try:
    user ={}
    number_of_users = int(input("Enter number of players: "))
    players_done = 0
    if number_of_users <= 0:
        print("enter a valid digit")
    while players_done < number_of_users:
        score = 0
    # while number_of_users != players_done:
        name = input("Enter your name: ")
        for question, answer in questions.items():
            print(question)
            Your_answer = input("Enter your answer: ").title()
            if Your_answer == answer:
                score = score + 50
                print("Correct")
                
            else:
                print("incorrect answer")


        user[name]=score
        players_done += 1

        print(f"{user}")
    all_scores =[]
    for name, score in user.items():
        all_scores.append(score)

    Highest = max(all_scores)
    print(f"the highest score is {name}:{Highest}")

except:
    print("invalid not a number")
    print("Enter a valid number")