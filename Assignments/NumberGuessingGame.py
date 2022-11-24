import random

# guess = int(input("Enter a number between 1 and 20: "))

computer_choice = random.randint(0,20)

# if computer_choice == guess:
#     print("You win!")
# else:
#     print(f"Sorry, you choose wrong number. Computer's choice was {computer_choice}")

chances = 5

for i in range(0,chances):
    guess = int(input("Enter a number between 1 and 20: "))
    if computer_choice == guess:
        print(f"You have won!")
        break
    else:
        if i != chances - 1:
            print("Sorry you chose a wrong number")
            print(f"You have {chances-i-1} attempts to guess the number")
            if guess > computer_choice:
                print("Try something low.")
            else:
                print("Try something high")
        else:
            print("You loose as you have completed all your attempts.")