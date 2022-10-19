# 1 – Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# Пример:
# 6782 -> 23
# 0,56 -> 11

from decimal import Decimal

number = Decimal(input('Enter the number: '))
while int(number) != number:
    number *= 10
sum = 0
while number:
    sum += number % 10
    number //= 10
print(abs(round((sum),0)))
