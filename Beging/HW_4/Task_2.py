# 2) Задайте натуральное число N.
# Напишите программу, которая составит список простых множителей числа N.

a = int(input('Enter a number:'))

list = []

list.append(1)

for i in range(2, a):
    if a % i == 0:
        a //= i
        list.append(i)
    else:
        i += 1
print(list)





