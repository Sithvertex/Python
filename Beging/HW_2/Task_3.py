# 3 – Задайте список из n чисел последовательности (1 + 1 / n) ** n и
# выведите на экран их сумму.
#
# Пример:
# 1 -> 2.0
# 2 -> 4.25
# 3 -> 6.62037037037037

data = []
N = int(input('Введите число N : '))

sum = 0
for i in range(1,N+1):
    num = (1+1/i)**i
    sum += num
    data.append(num)
print(data)
print(sum)
