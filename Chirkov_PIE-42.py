print("Task 1")
t = (([1, 2], ['012', 'abc']), [4, 3])
res = t[0][1][1][2]
print(res, "\n")

print("Task 2")
t = (
    42,
    3.1415,
    1 + 2j,
    ("Hello, World!",),
    (),
    []
)
res = t[3][0]
print("Строка из вложенного кортежа:", res, "\n")

print("Task 3")
matryoshka = (
    42,
    (
        3.1415,
        (
            1 + 2j,
            (
                "Конечная строка",
                ()
            )
        )
    )
)
res = matryoshka[1][1][1][0]
print("Конечная строка:", res, "\n")

print("Task 4")
t = (1, 2, 3, 4, 5)

one = t[0]
third = t[2]
slice = t[0:3]

one_n = t[-5]
third_n = t[-3]
slice_n = t[-5:-2]

print("Способ 1 (положительные индексы):")
print("Первый элемент:", one)
print("Третий элемент:", third)
print("Срез первых трех элементов:", slice)
print("\nСпособ 2 (отрицательные индексы):")
print("Первый элемент:", one_n)
print("Третий элемент:", third_n)
print("Срез первых трех элементов:", slice_n, "\n")

print("Task 5")
t = ((1, 2, ('Ok!', 3)), ('tuple', 4), 5)
res = t[0][2][0]
print(res, "\n")

print("Task 6")
t = (3, 's', 1, 5, 's')

total = len(t)
count_s = t.count('s')
first_s = t.index('s')

print(f"Количество всех элементов: {total}")
print(f"Количество строк 's': {count_s}")
print(f"Индекс первого вхождения 's': {first_s}", "\n")

print("Task 7")
t = (['кит', 1, 3], 5)

t[0][0] = 'кот'
t[0].remove(1)
t[0][-1] = 3 ** 2

print("Измененный кортеж:", t)

try:
    t[1] = t[1] * 2
except TypeError as e:
    print("Ошибка:", e)
print("\n")

print("Task 8")
def tpl_sort(tpl):
    # Проверяем, все ли элементы целые числа
    for element in tpl:
        if not isinstance(element, int):
            return tpl
    # Если все элементы целые, сортируем кортеж
    return tuple(sorted(tpl))

print(tpl_sort((3, 1, 2)))
print(tpl_sort((3, '1', 2)))
print(tpl_sort((5.5, 2, 1)))
print(tpl_sort(()), "\n")

print("Task 9")
def slicer(t, e):
    index = []
    for i, j in enumerate(t):
        if j == e:
            index.append(i)
    if not index:
        return tuple()
    elif len(index) == 1:
        return t[index[0]:]
    else:
        return t[index[0]:index[1] + 1]

print(slicer((1, 2, 3, 2, 4), 2))
print(slicer((5, 6, 7), 6))
print(slicer(('a', 'b', 'c'), 'd'))
print(slicer(('a', 'b', 'a', 'c'), 'a'), "\n")

print("Task 10")
students = (
    ("Анна", 20, 4.5, "Москва"),
    ("Иван", 22, 3.8, "Санкт-Петербург"),
    ("Мария", 21, 4.2, "Казань"),
    ("Петр", 19, 4.5, "Екатеринбург"),
    ("Ольга", 23, 4.8, "Новосибирск"),
    ("Дмитрий", 20, 4.1, "Краснодар"),
    ("Светлана", 22, 4.9, "Воронеж")
)

def good_students(students):
    total = 0
    count = 0
    for i in students:
        total += i[2]
        count += 1
    average = total / count if count > 0 else 0
    
    good_students = []
    for i in students:
        if i[2] >= average:
            good_students.append(i[0])
    
    print(f"Ученики {', '.join(good_students)} в этом семестре хорошо учатся!")

good_students(students)