#Table of a number
def multi():

    i = int(input("Enter a number: "))

    for j in range(1, 11):
        print(i, 'X', j, '=', i * j)

multi()