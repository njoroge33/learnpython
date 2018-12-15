# password generator weak or strong
import string
import random
upper = string.ascii_uppercase
lower = string.ascii_lowercase
num = string.digits
quiz = input("strong = s or weak = w : ")
psw = []

if quiz == "s":
    for i in range(8):
        psw.append(random.choice(upper + lower + num))
        print("".join(psw))
elif quiz == "w":
    for i in range(8):
        psw.append(random.choice(lower + num))
        print("".join(psw))