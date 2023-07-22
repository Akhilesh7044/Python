

#code to rename the call recordings with availabe data in their names 
#using regx and file hadling in python


import re, shutil

date_pattern=r"20+\d{6}"  #helps to find date (20 followed by 6 digits)
name_pattern=r"[a-zA-Z ( )]+\."  #helps to find name of person
number_pattern=r"\+91+\d{10}|\d{10}" # helps to find number either +91 followed by 10 digits or else 10 digit number
time_pattern=r"_\d{6}" # helps to find time

import os
song_dir="C:\\Users\\akhil\\Desktop\\Call"  # directory of call recording file
song_list=[]  # Empty list 

for root, dirs, files in os.walk(song_dir):
    song_list.append(files)  # it will append the call recordingsfilenames to song list

for text in song_list[0]: # itereate the call recording names
    date=re.findall(date_pattern,text) # find date in perticular recording
    print(date)
    name=["xyz"]
    if re.findall(name_pattern,text): # if number is saved it will save name as saved name else no chnage in xyz name as above
        name=re.findall(name_pattern,text)
    number=re.findall(number_pattern,text) #find the number 
    print(number)
    time=re.findall(time_pattern,text) # find time (later added since it is overwrite call recordings if call is happend multiple times same day)
    new_name="\\"+date[0]+time[0]+"_"+name[0]+"_"+number[0]+".m4a"  # concatinating hole new name of call recording as required from separated data 
    
    shutil.copy(f'C:\\Users\\akhil\\Desktop\\Call\\{text}',f'C:\\Users\\akhil\\Desktop\\New_Call{new_name}')  # simple copy with rename


# end of code
