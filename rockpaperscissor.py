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

#Write your code below this line 👇
import random as rn
li=[rock,paper,scissors]
num=int(input("Enter 0 for rock 1 for paper 2 for scissor"))
computerchoice=rn.choice(li)
print("computer choose\n",computerchoice)
choice=li[num]
print(f'Your choice{choice}')
if computerchoice==rock:
    if choice==paper:
        print("You Win")
    elif choice==rock:
        print("Draw")
    else:
        print("You Loose")
elif computerchoice==paper:
    if choice==paper:
        print("You Draw")
    elif choice==rock:
        print("You Loose")
    else:
        print("You Win")
else:
    if choice==paper:
        print("You Loose")
    elif choice==rock:
        print("You Win")
    else:
        print("Draw")