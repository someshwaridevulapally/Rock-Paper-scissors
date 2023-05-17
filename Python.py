import random

user_input= int(input('enter your choice "rock=0","paper=1","scissors=2"\n'))
#0
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
#1
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
#2
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print("your choice:")
choice = [rock, paper, scissors]
print(choice[user_input])
print("computer chose:")
computer_output = random.randint(0, 2)
print(choice[computer_output])

if user_input == 0 and computer_output == 1:
  print("you win") 
if user_input== 0 and computer_output== 2:
  print("you win") 
if user_input== 1 and computer_output == 0:
  print("you win") 
if user_input == 1 and computer_output == 2:
  print("you lose")
if user_input == 2 and computer_output == 0:
  print("you lose") 
if user_input== 2 and computer_output == 1:
  print("you win") 
if user_input == computer_output: 
  print("Its a tie")

