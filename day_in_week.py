#Determine the day of the week from number(1-7)

def weekday():
    c = int(input("Enter a number: "))
    switch = {
        1: "Monday",
        2: "Tuesday",
        3: "Wednesday",
        4: "Thursday",
        5: "Friday",
        6: "Saturday",
        7: "Sunday"
    }
    return switch.get(c)



print(weekday())
