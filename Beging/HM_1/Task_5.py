
x1,y1 = map(float, input('Enter the coordinates of the point x1 and y1 separated by commas: \n').split(','))

x2,y2 = map(float, input('Enter the coordinates of the point x2 and y2 separated by commas: \n').split(','))

print(' distance AB = ', round(((((x1 - x2) ** 2) + (y1 - y2) ** 2) ** (1/2)), 2))