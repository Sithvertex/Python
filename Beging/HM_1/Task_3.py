x = int(input('Enter a value on the x axis: '))
y = int(input('Enter a value on the y axis: '))

if x > 0 < y:
    print('the first half- plane')
elif x < 0 < y:
    print('the second half - plane')
elif x < 0 > y:
    print('the third half- plane')
elif x > 0 > y:
    print('the fourth half- plane')
elif x == 0 != y:
    print('A point on the ordinate axis')
elif x != 0 == y:
    print('A point on the abcis axis')
else:
    print('the center of the coordinate system')
