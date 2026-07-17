import random
print("Welcome To The Rock Paper Scissors Game!")

print()

choices = ["rock", "paper", "scissors"]
while True:
    while True:
        user = input("Rock Paper or Scissors?: ").lower()
        if user not in choices:
            print("Please pick a valid option. ")
            continue
        break
        

    computer = random.choice(choices)

    print(f"You chose {user}.")
    print(f"Computer chose {computer}.")

    if user == computer:
        print("DRAW!")
    elif user == "rock" and computer == "scissors":
        print("YOU WIN!")
    elif user == "rock" and computer == "paper":
        print("YOU LOSE!")
    elif user == "paper" and computer == "rock":
        print("YOU WIN!")
    elif user == "paper" and computer == "scissors":
        print("YOU LOSE!")
    elif user == "scissors" and computer == "paper":
        print("YOU WIN!")
    elif user == "scissors" and computer == "rock":
        print("YOU LOSE!")
    
    again = input("Play again? (y/n): ").lower()

    if again == "n":
        break

    






