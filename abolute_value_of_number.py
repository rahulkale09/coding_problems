#Find absolute value of a number

def absolute_value():
    num = float(input("Enter a number: "))
    if num >= 0:
        print(f"The absolute value of {num} is {num}.")
    elif num < 0:
        abs_value = -num
        print(f"The absolute value of {num} is {abs_value}")
    else:
        print('Number is invalid')

absolute_value()