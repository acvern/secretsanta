import random

"""
Alvern Chen
Secret Santa Name Organizer v0.1
Matches names to each other without the hassle of human contact!
Last modified September 15, 2016
"""

name_list = open("names.txt", "r")
names = []

for name in name_list.readlines():
    names.append(name.strip())
    
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
    
    final_list.write("%-24s" % "Giver" + "Receiver" + "\n")
    final_list.write("=" * 48 + "\n")
    
    for line in range(0, len(names)):
        final_list.write("%-24s" % names[line] + receive[line] + "\n")
    
    final_list.close()
            
    
main()
    
    