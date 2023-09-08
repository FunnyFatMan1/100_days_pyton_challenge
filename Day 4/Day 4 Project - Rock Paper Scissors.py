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
---.__(___)elections
'''
valid_choice = ["rock", "paper", "scissors"]
player_choice = input("What do you choose? Rock, Paper or Scissors.")
computer_choice = random.choice(valid_choice)
if player_choice == "rock" and computer_choice == "scissors":
    print("you win")
elif player_choice == "paper" and computer_choice == "rock":
    print("you win")
elif player_choice == "scissors" and computer_choice == "paper":
    print("you win")
elif player_choice != "rock" and player_choice != "paper" and player_choice != "scissors":
    print("type valid choice")
else:
    print("you loose")



