# 4) Задана натуральная степень k.
#  Сформировать случайным образом список коэффициентов
#  (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k.
# Пример:
# k=2 => 2x^2 + 4x + 5 = 0 или x^2 + 5 = 0 или 10x^2 = 0
import random
import numpy as np

k = int(input('Enter the degree of the polynomial: '))

asd = []

def function_wr():
    return random.randint(0, 101)

for i in range(k, 2, -1):
    poly = function_wr()
    if poly == 1:
        asd.append(f"x^{i}")
    elif poly == 0:
            i+=1
    else:
        asd.append(f"{poly}x^{i}")

if k > 2:
    poly = function_wr()
    asd.append(f"{poly}x^2")
    poly = function_wr()
    asd.append(f"{poly}x")
elif k == 2:
    poly = function_wr()
    asd.append(f"{poly}x^2")
    poly = function_wr()
    asd.append(f"{poly}x")
elif k == 1:
    poly = function_wr()
    asd.append(f"{poly}x")

poly = function_wr()
asd.append(f"{poly}")

equation_line = '+'.join(asd)+' = 0'

with open('file_2.txt', 'a') as file:
    file.write(equation_line + '\n')

print(equation_line)


