# 3. Задайте список из n чисел, заполненный по формуле (1 + 1/n) ** n и выведите на экран их сумму.

# in
#  6

# out
# [2.0, 2.25, 2.37, 2.441, 2.488, 2.522]
#  14.071

num = int(input())
sum_numbers = 0
list_numbers = []

for i in range (1,num + 1):
    result = round((1+1/i)** i, 3)
    list_numbers.append(result)
    sum_numbers += result

print(list_numbers)
print(sum_numbers)

