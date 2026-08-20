def check_triangle(a,b,c):
    if a+b>c and a+c>b and b+c>a:
        print("it is valid triangle")
    else:
        print("it is not a valid triangle")
        
a=int(input("Enter the side a:"))
b=int(input("Enter the side b:"))
c=int(input("Enter the side c:"))
check_triangle(a,b,c)