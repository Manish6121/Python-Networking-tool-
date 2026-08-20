def check_number(num):
    if num > 0:
        print("positive")
    elif num < 0:
        print("Negetive")
    else:
        print("Number is 0")

num = float(input("enter your number: "))
check_number(num)
