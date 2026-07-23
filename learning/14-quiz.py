questions = ("What is the capital of Turkey?",
             "Which planet is known as the Red Planet?",
             "What does CPU stand for?",
             "How many days are there in a leap year?",
             "What is the largest ocean on Earth?")

choices = (
("A. Ankara", "B. İzmir", "C. Konya", "D. İstanbul", "E. Antalya"),
("A. Uranus", "B. Neptune", "C. Jupiter", "D. Saturn", "E. Mars"),
("A. Central Process Unit", "B. Central Processing Unit", "C. Computer Personal Unit", "D. Central Power Unit","E. Computer Progressive Unit"),
("A. 365", "B. 364", "C. 366", "D. 367", "E. 368"),
("A. Indian Ocean", "B. Atlantic Ocean", "C. Pacific Ocean", "D. Arctic Ocean", "E. Southern Ocean")
)

answers = ("A", "E", "B", "C", "C")

guesses = []

score = 0

question_num = 0

for question in questions:
    print(question)
    for choice in choices[question_num]:
        print(choice)

    guess = input("Please Choose Your Answer(A, B, C, D, E): ").upper()

    guesses.append(guess)   

    if guess == answers[question_num]:
        print("CORRECT!")
        score += 1
    else:
        print("INCORRECT!")
        print(f"The correct answer was {answers[question_num]}.")
    
    question_num += 1

print(f"You got {score} questions right!")
