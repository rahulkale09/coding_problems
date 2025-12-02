#print sum of all the digits in a number

def sum_of_digits():
    n = int(input('Enter a number: '))
    total = 0
    while n != 0:
        digit = n % 10
        total = total + digit
        n = n // 10
    
    print("Sum of digits:", total)
sum_of_digits()