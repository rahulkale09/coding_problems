#check if number is palindrome
#from reverse_number import reverse_number
def is_palindrome():
    n = int(input('Enter a number: '))
    original = n
    rev = 0
    while n > 0:
        digit = n % 10
        rev =rev * 10 + digit
        n = n // 10
    n = original
    if n == rev:
        print(f"{n} is a palindrome")
    else:
        print(f"{n} is not a palindrome")

is_palindrome()
