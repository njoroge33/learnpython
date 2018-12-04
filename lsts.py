def print_less_than_num(num):
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    for i in a:
        if i < num:
            print(i)


num_input = int(input("enter a number: "))
print_less_than_num(num_input)
