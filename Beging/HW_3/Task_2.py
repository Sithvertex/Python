# 2)Напишите программу, которая найдёт произведение пар чисел списка.
# Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

data = [2, 3, 5, 6]
rn_list = []
if (len(data) % 2) == 0:
    N = len(data) // 2
else:
    N = len(data) // 2 + 1
for i in range(0, N):
    rn_list.append(data[i] * data[(len(data)-1)-i])
print(rn_list)
