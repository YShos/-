import random
from collections import Counter
n = int(input('Введите кол-во столбцов матрицы: '))
m = int(input('Введите кол-во строк матрицы: '))
matrix = [[random.randrange(0, 10) for y in range(n)] for x in range(m)]
print(*matrix, sep='\n')
most_common = [(i, Counter(x).most_common(1)[0]) for i, x in enumerate(matrix, start=1)]
print('(Номер строки, (элемент, количество повторяющихся элементов))')
print(*sorted(most_common, key=lambda x: int(x[1][1]), reverse=True), sep='\n')