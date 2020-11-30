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


while True:
    player = int(
        input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
    if player > 2:
        print("You've got an error, please check the instruction again.")
        continue
    else:
        break

if player == 0:
    print(rock)
elif player == 1:
    print(paper)
else:
    print(scissors)

print("Computer choose: ")
computer = random.randint(0, 2)
if computer == 0:
    print(rock)
elif computer == 1:
    print(paper)
else:
    print(scissors)

division = player - computer

if division == 1 or division == -2:
    print("You Win.")
elif division == 0:
    print("It's a Draw.")
else:
    print("You Lose.")
