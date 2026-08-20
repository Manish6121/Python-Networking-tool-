def check_character(ch):
    if ch.isupper():
        print(ch,"is uppercase")
    elif ch.islower():
        print(ch,"is lower")
    elif ch.isdigit():
        print(ch,"is digit")
    else:
        print(ch,"is special character")

ch = input("Enter the character: ")
check_character(ch)