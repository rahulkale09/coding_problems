import string


def letters():
    l = str(input("Enter a letter: "))
    if l == l.lower():
        print("Letter is in lowercase")
    else:
        print("Letter is uppercase")

letters()

