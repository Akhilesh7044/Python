


#guessing number

import random 
#1 save a random number in a variable from 1-100 
number=random.randint(1,100)


#3 Take a guess from user in a variable define a function
def make_a_guess(chances):
    guess_num=int(input(f"and you are having {chances} chances \nMake a guess: "))
    return guess_num

#2 define a function which will take that random number and tell how close are you if guessed num
def howclose(guess_num,number):
    if guess_num<number:
        print("Too low ")
        return 0
    elif guess_num>number:
        print("Too High")
        return 0
    else:
        print("great! Your guess is correct")
        return 1
    
    

diff_level=input("What difficulty level you want to choose?  'easy' or 'hard'\n") 
print("I am thinking a number from 1 to 100 ")
gameover=0
if diff_level=='easy':
    chances=10
else:
    chances=5   
        
is_correct=False

while (not is_correct) and chances:
    guess_num=make_a_guess(chances)
    guess_num=int(guess_num)
    is_correct=howclose(guess_num,number)
    if  is_correct:
        is_correct=True
    else: 
       
        chances-=1
        if chances==0:
            gameover=1
        print(f"Incorrect Guess ! \nYou have {chances} chances left !\n ")
        if gameover:
            print("Gave Over !")
            
            
            
            
            
