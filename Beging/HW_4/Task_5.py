# 5) Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.
import re
from sympy import Symbol, collect

# a = bool("1")
# b = bool(a - 2)
# print(b)

with open('file_1.txt', 'r') as data1:
    first = data1.readline()
with open('file_2.txt', 'r') as data2:
    second = data2.readline()

def splite(equal):
    equal = re.sub(r'(\d)(x)', r'\1*\2', equal)
    equal = equal.replace('^', '**')
    equal = equal[:-4:]
    return equal
def splite_two(equal):
    equal = equal.replace('**', '^')
    equal = equal.replace('*', '')
    equal = equal + ' = 0'
    return equal

x = Symbol('x')

symply_1 = splite(first)
symply_2 = splite(second)

# arr = first.split('+')
# arr2 = second.split('+')
# i = 0
# while True:
#     if len(arr) > len(arr2):
#         arr2.insert(i, 0)
#         i +=1
#     elif len(arr2) > len(arr):
#         arr.insert(i, 0)
#         i +=1
#     elif len(arr) == len(arr2):
#         break

thirth = splite_two(str(collect(symply_1 + ' + ' + symply_2, x)))

with open('result.txt', 'w') as frame:
    frame.write(thirth)
