def f(a,b,c):
    if a > b and a > c:
        print(a, "is greater than", b, "and", c)
    elif b > a and b > c:
        print(b, "is greater than", a, "and", c)
    else:
        print(c, "is greater than", a, "and", b)

a = int(input("Enter Your First Number: "))
b = int(input("Enter Your Second Number: "))
c = int(input("Enter Your Third Number: "))
f(a,b,c)
