import random

user = None
computer = random.choice(['rock', 'paper', 'scissor'])

while user is None:
    user = input("Enter the value you wish to choose:")
    if user not in ['rock', 'paper', 'scissor']:
        print("PLease choose valid values")
        user = None

if user == computer:
    print("Draw")
if user == 'rock':
    if computer == "paper":
        print("Computer wins")
    elif computer == "scissor":
        print("user wins")
if user == 'paper':
    if computer == "scissor":
        print("Computer wins")
    elif computer == "rock":
        print("user wins")
if user == 'scissor':
    if computer == "rock":
        print("Computer wins")
    elif computer == "paper":
        print("user wins")

print('computer is {}'.format(computer))
print('user is {}'.format(user))
