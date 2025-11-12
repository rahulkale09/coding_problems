#Check whether the number is divisible by 5 and 11

def divisible_number():
    n = int(input('Enter a number: '))
    if n % 5 == 0 and n % 11 == 0:
        print("Number is divisible by 5 and 11")
    else:
        print("Number is not divisible by 5 and 11")
divisible_number()