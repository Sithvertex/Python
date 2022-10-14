import numpy as np

# for X in (0,1):
#     for Y in (1,0):
#         for Z in (0,1):
#             if not (X or Y or Z) == (not X and not Y and not Z):
#                 print('True')
#                 print(X,Y,Z)
#             else:
#                 print('False')

print(all(not (x or y or z) == (not x and not y and not z) for x in range(2) for z in range(2) for y in range(2)))