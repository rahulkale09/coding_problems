#check whether the angles form a valid triangle

def triangle_check():
    a = int(input('Enter first angle:'))
    b = int(input('Enter second angle:'))
    c = int(input('Enter third angle:'))

    if a > 0  and b > 0 and c > 0 and (a + b + c) == 180:
        print('The angles form a valid triangle.')
    else:
        print('The angles do not form a valid triangle.')
    
triangle_check()