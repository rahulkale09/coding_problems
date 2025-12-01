#Calculate the grade based on scores

def grade_calculation():
    score = float(input('Enter your score (0-100): '))
    if 90 <= score <= 100:
        print('Your grade is A.')
    elif 80<= score < 90:
        print('Your grade is B.')
    elif 70 <= score < 80:
        print('Your grade is C.')
    elif 60 <= score < 70:
        print('Your grade is D.')
    elif 40 <= score < 60:
        print('Your grade is F.')
    elif 0 <= score < 40:
        print('Your grade is Fail.')
    else:
        print('Invalid score. Please enter a score between 0 and 100.')
grade_calculation()
