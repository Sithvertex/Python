# 1) Вычислить число c заданной точностью d
# Пример:
# при d = 0.001, π = 3.142 10^(-1) ≤ d ≤10^(-10)

a = float(input('Enter a number separated by a dot :'))
N = int(input('Enter the accuracy by which digit after the point to calculate :'))

print(f'{a:.{N}f}')
