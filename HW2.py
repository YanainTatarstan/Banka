# 1.Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у пользователя, а указать явно, в программе.

num_i = -9
num_f = 5.1
sys = ~6
m_bin = bin(8)
text = "Хо хо хо"
m_list = [1, 4]
tup = (1, 7)
m_dict = {1: "hedgehog", 2: "cockoos"}

super_puper_list = [num_i, num_f, m_bin, sys, text, m_list, tup, m_dict]
for elem in super_puper_list:
    print(f"{elem} is {type(elem)}")

# или

super_puper_list = [-9, 5.1, True, False, None, "Ho_ho_ho", {1, 2}, [1, "coc"], (1, 4), {1: "hedgehog", 2: "cockoos"}]
for elem in super_puper_list:
    print(type(elem))

# 2.Для списка реализовать обмен значений соседних элементов. Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т. д. При нечётном количестве элементов последний сохранить на своём месте. Для заполнения списка элементов нужно использовать функцию input().

super_puper_list = int(input('Введите количество элементов в списке: '))

ind = []
for i in range(super_puper_list):
    j = input()
    ind.append(j)
for i in range(0, len(ind) - 1, 2):
    ind[i], ind[i + 1] = ind[i + 1], ind[i]
ind

# 3.Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить, к какому времени года относится месяц (зима, весна, лето, осень). Напишите решения через list и dict.

number = int(input("Введите номер месяца (от 1 до 12): "))
if number == 1 or number == 2 or number == 12:
    print("Зима")
elif number == 3 or number == 4 or number == 5:
    print("Весна")
elif number == 6 or number == 7 or number == 8:
    print("Лето")
elif number == 9 or number == 10 or number == 11:
    print("Осень")
else:
    print(f"Месяца под номером {number} не существует ")

# 4. Пользователь вводит строку из нескольких слов, разделённых пробелами. Вывести каждое слово с новой строки. Строки нужно пронумеровать. Если слово длинное, выводить только первые 10 букв в слове.

word = input("Укажите Ваше полное ФИО ")
word_a = word.split(" ")
for i, el in enumerate(word_a):
    print(f"{i + 1}: {el[:10]}".title())

# 5. Реализовать структуру «Рейтинг», представляющую собой набор натуральных чисел, который не возрастает. У пользователя нужно запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями, то новый элемент с тем же значением должен разместиться после них. Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2. Пользователь ввёл число 3. Результат: 7, 5, 3, 3, 3, 2. Пользователь ввёл число 8. Результат: 8, 7, 5, 3, 3, 2. Пользователь ввёл число 1. Результат: 7, 5, 3, 3, 2, 1. Набор натуральных чисел можно задать сразу в коде, например, my_list = [7, 5, 3, 3, 2].

raiting = []

while True:
    spi = input("Введите целое число: ")
    if not spi.isdigit():
        print("Что-то пошло не так, попробуйте еще ")
        continue
    else:
        num = int(spi)
    idx = None
    for i, num in enumerate(raiting):
        if spi > num:
            idx = i
            break
    if idx is None:
        raiting.append(spi)
    else:
        raiting.insert(idx, spi)
    print(raiting)

# 6.Реализовать структуру данных «Товары». Она должна представлять собой список кортежей. Каждый кортеж хранит информацию об отдельном товаре. В кортеже должно быть два элемента — номер товара и словарь с параметрами, то есть характеристиками товара: название, цена, количество, единица измерения. Структуру нужно сформировать программно, запросив все данные у пользователя.

tovar = []
analyse_tovar = {"Название": [], "Цена(руб)": [], "Количество": [], "Ед. изм.": []}

num = 1
while True:
    if input("Хотите добавить товар? +/-: ").lower() == "+":
        name = input("Название: ")
        price = input("Цена(руб): ")
        cnt = input("Количество: ")
        unit = input("Ед. изм.: ")

        tovar.append((num, {"Название": name, "Цена(руб)": price, "Количество": cnt, "Ед. изм.": unit}))
        num += 1
    else:
        break
for item in tovar:
    name_list = analyse_tovar["Название"]
    price_list = analyse_tovar["Цена(руб)"]
    cnt_list = analyse_tovar["Количество"]
    unit_list = analyse_tovar["Ед. изм."]

    name_list.append(item[1]["Название"])
    price_list.append(item[1]["Цена(руб)"])
    cnt_list.append(item[1]["Количество"])
    unit_list.append(item[1]["Ед. изм."])

print = tovar


