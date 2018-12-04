name = input("enter a sentence!")
if name[0::].lower() == name[::-1].lower():
    print("it's a palindrome")
else:
    print("it's not a palindrome")
