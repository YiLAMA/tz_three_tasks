# сложность big O(n)
def task(array):
    """
    Находит индекс первого нуля (место, где заканчиваются единицы и начинаются нули).
    """
    ind = 0
    zero = False
    for i, a in enumerate(array):
        if array[i] == '0':
            ind = i
            zero = True
            break
    if zero:
        return ind
    else:
        return f'Ошибка: Отсутствует ноль'


# сложность логарифмическая, big O(log2 n). Будет работать намного быстрее.
def task_bin(array):
    """
    Находит индекс первого нуля (место, где заканчиваются единицы и начинаются нули)
    через бинарный поиск.
    """
    zero = False
    begin = -1
    end = len(array)
    while end > begin + 1:
        middle = (begin + end) // 2
        if array[middle] == '0':
            zero = True
            end = middle
        else:
            begin = middle
    if zero:
        return end
    else:
        return f'Ошибка: Отсутствует ноль'


test1 = "111111111111111111111111100000000"
test2 = "1111111111111111111111111111111111111111111111111111111111111000"
test3 = "1110000000000000000000000000000000000000000000000000000000000000"
test4 = "1111"
test5 = "0000"
test6 = "10"
test7 = "1"
test8 = "0"
test9 = ""

list_test = [
    "111111111111111111111111100000000",
    "1111111111111111111111111111111111111111111111111111111111111000",
    "1110000000000000000000000000000000000000000000000000000000000000",
    "1111",
    "0000",
    "10",
    "1",
    "0",
    "",
]

print(task(test1))

print(task_bin(test1))

# for i,test in enumerate(list_test):
#     print(f"---Входные данные №{i+1}: {test} \nРезультат: {task_bin(test)}")
