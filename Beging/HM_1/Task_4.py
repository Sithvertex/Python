number = int(input('Enter the number of the coordinate quarter: '))

if 1 <= number <= 4:
    if number == 1:
        print('The range of change of coordinates of the first quarter: x > 0 y > 0')
    elif number == 2:
        print('The range of changes in the coordinates of the second quarter: x < 0 y > 0')
    elif number == 3:
        print('The range of changes in the coordinates of the third quarter: x < 0 y < 0')
    elif number == 4:
        print('The range of change in the coordinates of the fourth quarter x > 0 y < 0')
else:
    print('Incorrect data entered')