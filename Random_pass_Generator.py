




#Password Generator Project
# This Project will Generate Random Password with user defined no. of letters, Symbols and numbers
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

pas=[]
for i in range(nr_letters):
  j=random.choice(letters)

  pas.append(j)


for i in range(nr_symbols):
  j=random.choice(symbols)
  pas.append(j)


for i in range(nr_numbers):
  j=random.choice(numbers)
  pas.append(j)


#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
st=''
for i in pas:
  st=st+i

print(f" Normal Password with Letters,Sysmbols and numbers Respectively: {st}")



#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&

# here we have to shuffel the list and for the we have to use shuffel() function

random.shuffle(pas) # list is shuffeled 
# again we have to convert it in string
str2=''
for i in pas:
  str2+=i
print(f" Strong Password with same Chracters Shuffled: \t\t\t {str2}")





