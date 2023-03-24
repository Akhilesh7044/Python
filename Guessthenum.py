



import random
print("Hi, What is your name ?")
name=input()
print("Hello "+name+", i am thinking a number between 0-20. I think you can guess it \n")
secreatenum=random.randint(0,21)

for i in range(6):
    try :
        print("Make a guess: ")
        num=int(input())
        if num<secreatenum:
            print("No, it is Greater than this \n")
        elif num>secreatenum:
            print("No, it is Less than this \n")
        elif num==secreatenum:
            print("Great! You got it in "+str(i+1)+" Trails\n")
            i=i-1
            break
    except ValueError:
        print("Please Enter Numbers Only ! \n")
if i==5:
    print(" Ohh. i am thinking of number "+str(secreatenum)+" . It's Ok.\n")


    
    
    
