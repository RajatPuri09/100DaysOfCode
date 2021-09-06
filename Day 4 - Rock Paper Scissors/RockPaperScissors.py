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

img = [rock, paper, scissors]

user_choice = int(input("Choose. Type 0 for ROCK, 1 for PAPER, 2 for SCISSORS\n"))
print("User choice:", img[user_choice])

CPU_choice = random.randint(0,2)
print("CPU choice:", img[CPU_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and CPU_choice == 2:
  print("You win!")
elif CPU_choice == 0 and user_choice == 2:
  print("You lose")
elif CPU_choice > user_choice:
  print("You lose")
elif user_choice > CPU_choice:
  print("You win!")
elif CPU_choice == user_choice:
  print("It's a draw")