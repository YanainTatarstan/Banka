
print(3 / 2)
print(8 // 2)
print(2 + 4)
print(2 * 4)

a = 12
b = a + 8
print("12 + 8 = ", b)

name = input("Enter your name: ")
print("Hello, %s!" % name)

a = input("Enter your name: ")
b = int(input("Enter your age: "))
c = int(input("Enter any number: "))
print(f"Ваше имя: {a}")
print(f"Ваш возраст: {b}")
print(f"Ваш номер телефона: {c}")

time_in_sec = int(input("Введите время в секундах: "))
hours = time_in_sec // 3600
residue = time_in_sec % 3600
minutes = residue // 60
sec = residue % 60
print(f"{time_in_sec} секунд, это: {hours} ч; {minutes} мин; {sec} сек ")

number_n = int(input("Введите целое число n (от 1 до 99999): "))
while number_n >= 1 and number_n <= 99999:
    a = int(number_n + number_n)
    b = int(number_n + number_n + number_n)
    sum = int(number_n) + a + b
    print(f"Число n равно - {number_n}; Сумма чисел n + nn + nnn равна - {sum}")
    break
else:
    var = number_n <= 1 and number_n >= 99999
    print("Вы ввели более 99999 или менее 1, попробуйте еще раз")

number = input("Введите любое целое число (напр. 12345): ")
x = 0
for i in number:
    while int(i) > x:
        x = int(i)
print("Самая большая цифра в числе: ", x)

n = int(input("Введите любое целое число (напр. 12345): "))
max = n % 10
while n >= 1:
    n = n // 10
    if n % 10 > max:
        max = n % 10
    if n > 9:
        continue
    else:
        print("Самая большая цифра в числе ", max)
        break

profit = float(input("Введите прибыль за квартал, руб.: "))
loss = float(input("Введите расходы за квартал, руб.: "))
if profit > loss:
    profitability = profit - loss
    rent = profitability / profit
    print(f"Отличная работа! Ваша рентабельность: {profitability} руб.")
    worker = int(input("Введите численность всех работников компании: "))
    print(f"{profitability/worker} прибыль в расчете на одного работника")
elif profit == loss:
    print("Ваши доходы равны расходам. Обратите внимание! ")
else:
    print("Расходы привышают доходы. Необходимо проверить введённые данные, либо бухгалтерскую отчетность!")

a = float(input("Введите результат первого дня пробежки, км: "))
b = float(input("Введите желаемый конечный результат, км: "))
day_1 = 1
if a > b:
    print(day_1)
while a < b:
    a = a + a/10
    day_1 += 1
print(f"На {day_1} день Вы достигните желаемых результатов - не менее {b} км")