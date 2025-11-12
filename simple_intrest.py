#Calculate the simple interest

def interest():
    p = float(input('Enter the principle amount:'))
    r = float(input('Enter the rate of interest:'))
    t = float(input('Enter the time in years:'))

    SI = (p*r*t) / 100
    print('Intrest is :', SI)

interest()