# 2. Задайте список, состоящий из произвольных слов, количество задаёт пользователь.
#    Напишите программу, которая определит индекс второго вхождения строки в списке
#    либо сообщит, что её нет.

from random import sample

def spisok (count, world = "abc"):
    my_list = []
    for i in range(count):
        temp = sample(world, k=3)
        my_list.append("".join(temp))
    return my_list
def index_find (world_2, sum_list):
    if world_2 in sum_list and sum_list.count(world_2) > 1:
        index1 = sum_list.index(world_2)
        print (sum_list.index(world_2, index1 + 1))
    else:
        print (- 1)

my_list1 = spisok(int(input()))
print (my_list1)
index_find (input(),my_list1)



