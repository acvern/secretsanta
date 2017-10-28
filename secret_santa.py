import random

"""
Alvern Chen
Secret Santa Name Organizer v0.2
Matches names to each other without the hassle of human contact!
Last modified November 29, 2016
"""

name_list = open("names.txt", "w")
names = ["Alex", "Alvern", "Benny", "Benson"] + \
      ["Calvin", "Franklin", "Jeffrey", "Josephine", "Joyce"] +\
      ["Justin", "Kelvin", "Kris", "Matthew", "Nathan"] +\
      ["Richard", "Sabrina", "Vishal", "Youeel", "Yuanxin", "Zoe"]

for name in range(0, len(names)):
    if name == (len(names) - 1):
        name_list.write(names[name])
    else:
        name_list.write(names[name] + " ")
    
name_list.close()

def main():
    #Write a give/receive pair to a file one at a time, checking
    #both that they are not already in the list and not the same person
    
    final_list = open("final.txt", "w")
    receive = []
    for name in range(0, len(names)):
        receiver_temp = random.randint(0, len(names) - 1)
        while (receiver_temp == name) or (names[receiver_temp] in receive):
            receiver_temp = random.randint(0, len(names) - 1)
        receive.append(names[receiver_temp])
    
    final_list = open ("final.txt", "w")
    
    for line in range(0, len(names)):
        if line == (len(names) - 1):
            final_list.write(receive[line])
        else:
            final_list.write(receive[line] + " ")
    
    final_list.close()
            
    
main()
    
    
