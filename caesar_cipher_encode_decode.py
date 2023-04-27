
# this Program is Used to encode and decode the a message of text 


logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88          
"""




print(logo)
alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]
# Taken alphabet 2 times since z is comes to encode by 5 shifts then it will againg consider a,b,c,d etc rather than producing error of out of index 

def caesar(start_text, shift_amount, cipher_direction):
# This function is used to shift the each character by specified shift number 
    end_text = ""  # Defined a empty String
    if cipher_direction == "decode":
        shift_amount *= -1  # if decode  then we have to subtract a shift_amount so by this it will be negative 
    for char in start_text: 
# Each character will be one by one come into char variable
      if char in alphabet: 
# if any non alphabet comes like a space or a symbol or a number it will not execute this if block so it will execute else block

        position = alphabet.index(char)
        new_position = position + shift_amount
        end_text += alphabet[new_position]
      else:
# no change it will simply concatinate the character to string
        end_text+=char

    print(f"Here's the {cipher_direction}d result: {end_text}")
# here in the place of cipher_direction encode of decode somes and it will becomes encoded or decoded resp.

is_continue=True
# True for 1st time 
while is_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % 26
    caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    command = input("Type 'yes' if you want to go again. Otherwise type 'no'")
    if command=='no':
     is_continue=False
# if user says no to run again then this will be False and end of the loop and program 





