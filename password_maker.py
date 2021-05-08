# This was written by K4WNR
# You have the free reign to change/alter this code
# if anyone has any suggestions on
import random
import os
import time
a = 0
e = 0
# the list(x) lists are the 4 main types of characters for passwords
# ,yes this can be done with unicode or ascii
# ,i'll fix it in future if i find other solution
list1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
list2 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V',
         'W', 'X', 'Y', 'Z']
list3 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
list4 = ["!", "#", "$", "%", "&", "(", ")", "*", "~", " ", "+", ",", "-", ".", "/", ":", ";", "<", ">", "@", "?", "=",
         "[", "]", "{", "^", "`", "_", "|", "}"]
new_list = list1 + list2 + list3 + list4

while a != "n":
    e = int(input("length: "))
    if e >= 8:
        break
    else:
        a = input("""this is a very short password
        for casual security it is recommended to use at least 8 characters long
        for basic security you should be using 20 characters long
        would you like to repeat: n for no """)
h = int(input("how many passwords: "))
p = []
for n in range(h):
    for i in range(e):
        x = random.choice(new_list)
        p.append(x)
    print("".join(p))
    p = []
print("you have 4 hours to save these passwords")
time.sleep(14400)
os.system("cls")
