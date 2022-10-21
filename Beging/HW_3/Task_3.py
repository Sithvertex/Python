# 3)Задайте список из вещественных чисел.
# Напишите программу, которая найдёт разницу между максимальным
# и минимальным значением дробной части элементов.
# Пример:
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.2

data = [1.1, 1.2, 3.1, 5, 10.01]
new_list = [round(data[i] % 1, 2) for i in range(0, len(data))]
max_num = 0
min_num = 0
for i in range(0, len(new_list)):
    if max_num < new_list[i]:
        max_num = new_list[i]
    elif min_num > new_list[i]:
        min_num = new_list[i]
print((max_num - min_num))