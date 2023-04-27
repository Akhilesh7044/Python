



import random
rps_id=['Rock','Paper', 'Scissors']
rps=[
"""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""", 
"""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""", 
"""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
]
# Taken For Printing
x=random.randint(0,2)
# Will generat random numbers from 0 to 2
z=int(input("What is your choice? Enter 1 for Rock, 2-Paper, 3-Scissors"))
y=z-1
# taken choice and decremented for indexing

#Just Printing Choices and Respected Ascii Art
print(f"Your choice is {rps_id[y]}\n{rps[y]}")
print(f"Computer choice is {rps_id[x]}\n{rps[x]}")


# Logic for Win and Loss
# y is user choice-1 so that indexing will be same for x and y  i.e. 0-Rock, 1-Paper, 2-Scissors
if y==0:
    if x==2:
        print("You Win!")
    elif x==1:
        print("You Lose! Better luck Next Time ")
    else:
        print("It's Tie!")
# Logic 

# if user choice is Rock then :
# for computer choices- 
# paper- You Lose
# scissors- You Win
# else(same)- Tie


if y==1:
    if x==0:
        print("You Win!")
    elif x==2:
        print("You Lose! Better luck Next Time ")
    else:
        print("It's Tie!") 
# Logic 

# if your choice is paper then :
# for computer choices- 
# Rock- You Win
# scissors- You Lose
# else(same)- Tie
              



if y==2:
    if x==1:
        print("You Win!")
    elif x==0:
        print("You Lose! Better luck Next Time ")
    else:
        print("It's Tie!")
# Logic 

# if Your choice is Scissors then :
# for computer choices- 
# Rock- You Lose
# Paper- You win
# else(same)- Tie




