#reverse the given number
def reverse_number():
    num = int(input("Enter a number: "))
    rev = 0
    while num > 0:
        digit = num % 10
        rev = rev * 10 + digit
        num = num // 10
    print("Reversed Number:", rev)
    return rev
    

reverse_number()