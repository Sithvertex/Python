# 3) Задайте последовательность чисел.
# Напишите программу, которая выведет
# список неповторяющихся элементов исходной последовательности.

data = [1, 1, 3, 4, 4, 75, 4, 8, 967, 2]

fin_list = [i for i in set(data)]

print(fin_list)
