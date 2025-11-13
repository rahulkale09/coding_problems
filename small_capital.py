import string


def letters():
    l = input("Enter a letter: ")
    if l.islower():
        print("Letter is in lowercase")
    elif l.isupper():
        print("Letter is in uppercase")
    elif l.isdigit():
        print("Letter is in numbers")
    else:
        print("Its a special letter")

letters()

