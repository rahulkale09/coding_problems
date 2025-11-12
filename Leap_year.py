#Check whether the year mentioned is leap year

def year():
    n = int(input('Enter a year: '))

    if n % 4 == 0 and n % 100 != 0 or n % 400 ==0:
        print('The year is leap year')
    else:
        print('The year is not leap year')

year()
