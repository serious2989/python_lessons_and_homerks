# 4. * Функция принимает в качестве аргументов строки в формате «Имя Фамилия»,
#      возвращает словарь, ключи — первые буквы фамилий, значения — словари,
#      реализованные по схеме предыдущего задания.

from collections import OrderedDict


def thesaurus_adv(*args):
    s_n_sort = {}
    for s_n in args:
        s_n_sort.setdefault(s_n.split()[1][0], {}).setdefault(s_n.split()[0][0], []).append(s_n)
    return dict(OrderedDict(sorted(s_n_sort.items(), key=lambda x: x[0])))


fio_name = thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев",
                         "Илья Иванов", "Анна Савельева", "Юнона Ветрякова",
                         "Борис Аркадьев", "Антон Серов", "Павел Анисимов")
print(fio_name)