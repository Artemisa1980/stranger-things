import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]
name = input("Enter your name: ")
ComputerScore = 0
PlayerScore = 0
NumberOfRounds = 0
gameOn = True
print(f"Welcome {name.title()}")

while gameOn:
  
  user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
  if user_choice not in [0, 1, 2]:
     print("Invalid input. Please enter 0 for Rock, 1 for Paper or 2 for Scissors.")
     continue
  print(f"{name.title()} option {user_choice}")
  print(game_images[user_choice])
  computer_choice = random.randint(0, 2)
  print(f"Computer option {computer_choice}")
  print(game_images[computer_choice])
  NumberOfRounds += 1
  if computer_choice == user_choice:
     print("Tie") 
  elif user_choice == 0 and computer_choice == 2:
     print("You win 🤓!")
     PlayerScore += 1
  elif computer_choice == 0 and user_choice == 2:
     print("You lose 😡")
     ComputerScore += 1
  elif computer_choice > user_choice:
     print("You lose 😡")
     ComputerScore += 1
  elif user_choice > computer_choice:
     print("You win 🤓!")
     PlayerScore += 1
  else:
     print("Choose a valid option to play this game")  
 
  
  print("----------------------")
  print("")
  print(f"Round No: {NumberOfRounds}")
  print("------ Score Board ------")
  print(f"{name.title()}: {PlayerScore} | Computer: {ComputerScore}")
  print("==================================")
  print("")
  if NumberOfRounds == 5:
    gameOn = False
    break
if PlayerScore == ComputerScore:
    print("Draw!!")
elif PlayerScore > ComputerScore:
    print(f"Congrats {name.title()}, You won the game 👏🏻!!")
else:
    print(f"Oops Compu won the game 🕺🏻!! Better luck next time {name.title()}!")  

####### Debugging challenge: #########
#Try running this code and type 5.
#It will give you an IndexError and point to line 32 as the issue.
#But on line 38, we are trying to prevent a crash by detecting
#any numbers greater than or equal to 3 or less than 0.
#So what's going on?
#Can you debug the code and fix it?
