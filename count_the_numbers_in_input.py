#count the numbers in input
def count_numbers():
    n = int(input("Enter a number: "))

    count = 0
    while n != 0:
        n = n // 10
        count = count + 1
    print("Number of digits:", count)
count_numbers()