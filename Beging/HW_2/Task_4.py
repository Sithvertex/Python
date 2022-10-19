# 4 – Задайте список из N элементов, заполненных числами из промежутка [-N, N].
# Найдите произведение элементов на указанных позициях. Позиции хранятся в файле
# file.txt в одной строке одно число
import random

n = int(input('Количество элементов N : '))
rn_list = random.sample(range(-n, n), n)
print('Random list: ', rn_list)

sum = 1
finish_list = []

with open('file.txt', 'r') as file:
    for i in file:
        if -len(rn_list) <= int(i) < len(rn_list):
            sum *= rn_list[int(i)]
            finish_list.append(rn_list[int(i)])

print('Sum = ', sum if sum != 1 else 'Значение не найдены')
