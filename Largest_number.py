#Compare 2 numbers and show the largest one

def largest_number():
    n1 = int(input('Enter the first number: '))
    n2 = int(input('Enter the second number: '))
    if n1 > n2:
        print('The number you entered first is greater')
    else:
        print('The number you entered second is greater')
largest_number()