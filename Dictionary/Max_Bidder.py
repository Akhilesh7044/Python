




import os
def cls():
    os.system("cls")

data={}
val=[]


def add_data(name,price):
    data[name]=price

def maxbidder(x):
    for key in data:
        if data[key]==x:
            break
    print(f"{key} is winner since he bided max amount of ${data[key]}")



def val_extracter():
    for key in data:
        val.append(data[key])
    x=max(val)
    maxbidder(x)
    

is_conti=True
while is_conti:
    print("Welcome to the Biding Program.")
    name=input("What is Your name?  ")
    price=int(input("What is your Biding Price? $"))
    add_data(name,price)
    yn=input("Did anyone want to bid? type 'yes' or 'no'")
    if yn=='yes':
        cls()
    else:
        is_conti=False
        val_extracter()










