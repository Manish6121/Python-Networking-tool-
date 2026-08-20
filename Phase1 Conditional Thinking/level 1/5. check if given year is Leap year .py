def d(year):
    if year%4==0:
        print(year,"this is leap year" )
    else:
        print(year,"this is not a leap year")
year=int(input("enter your year:"))
d(year)
