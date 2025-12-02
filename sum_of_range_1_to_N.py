#print the sum of numbers from 1 to N

def sum_of_range():
    n = int(input("Enter a number: "))
    total = 0
    for i in range(1, n + 1):
        total+= i
        print(total)
sum_of_range()