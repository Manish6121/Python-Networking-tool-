def c(num):
    if num%5==0 and num%3==0:
        print("it is divisible of 5 and 3")
    else:
        print("this is not divisible of 5 and 3")
num = float(input("enter your number: "))
c(num)