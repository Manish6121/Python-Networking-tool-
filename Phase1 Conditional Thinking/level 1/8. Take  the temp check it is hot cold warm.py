def check_temp(temp):
    if temp>30:
        print("it is hot")
    elif temp<20:
        print("it is cold")
    else:
        print("it is warm")

temp = int(input("Enter the Temp:"))
check_temp(temp)