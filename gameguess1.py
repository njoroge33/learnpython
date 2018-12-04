import random
a = random.randint(1, 9)

play = True
while play:
    b = int(input("guess a number"))
    if b == a:
        print("you win")
    elif b+1 == a or b-1 == a:
        print("you were almost there!")
    elif b == 0:
        play = False
    else:
        print("you missed with a big margin")