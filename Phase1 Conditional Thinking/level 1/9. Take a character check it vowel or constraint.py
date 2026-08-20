def check_Alphabet(ch):
    ch = ch.lower()
    if len(ch) == 1 and ch.isalpha():
        if ch in ['a', 'e', 'i', 'o', 'u']:
            print("It is a Vowel")
        else:
            print("It is a Consonant")
    else:
        print("Invalid input! Please enter a single letter.")

ch = input("Enter a character: ")
check_Alphabet(ch)
