# 5)Задайте число. Составьте список чисел Фибоначчи,
# в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так:
#  [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

N = int(input('Number :'))
fiban = []
not_fiban = []
for i in range (N+1):
    if i == 0:
        fiban.append(0)
    elif i == 1:
        fiban.append(1)
    else:
        fiban.append(fiban[i-1]+fiban[i-2])
for j in range(N, 0, -1):
    not_fiban.append(((-1) ** (j+1))*fiban[j])
print(not_fiban + fiban)