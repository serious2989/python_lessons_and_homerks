# ** 5. Реализуйте алгоритм перемешивания списка.
# Без функции shuffle из модуля random.

# 10
# -> [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# -> [0, 7, 6, 3, 4, 2, 9, 5, 1, 8]

from random import randrange

num = int(input())
numbers_list = list(range(num))
result_list = []

print(numbers_list)

for i in range(num):
    a, b = randrange(num), randrange(num)
    numbers_list[a], numbers_list[b] = numbers_list[b], numbers_list[a]

print(numbers_list)    