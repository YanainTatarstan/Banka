# 1.Создать класс TrafficLight (светофор). определить у него один атрибут color (цвет) и метод running (запуск); атрибут реализовать как приватный; в рамках метода реализовать переключение светофора в режимы: красный, жёлтый, зелёный; продолжительность первого состояния (красный) составляет 7 секунд, второго (жёлтый) — 2 секунды, третьего (зелёный) — на ваше усмотрение; переключение между режимами должно осуществляться только в указанном порядке (красный, жёлтый, зелёный); проверить работу примера, создав экземпляр и вызвав описанный метод. Задачу можно усложнить, реализовав проверку порядка режимов. При его нарушении выводить соответствующее сообщение и завершать скрипт.

import time
import os
os.system("color")
c = {
    'YELLOW': '\033[93m',
    'GREEN': '\033[92m',
    'RED': '\033[91m',
    'END': '\033[0m'
}

class TrafficLight:
    __color = 'Светофор'

    def running(self):
        print(f'!ЗАПУСК!')
        time.sleep(1)
        while True:

            print('\n''\033[91;1mКРАСНЫЙ\033[0m\n')
            time.sleep(1)
            sec = 7
            while True:
                print(sec, end=' ')
                time.sleep(1)
                sec -= 1
                if sec == 0:
                    break

            print('\n''\033[93;1mЖЕЛТЫЙ\033[0m\n')
            time.sleep(1)
            sec = 2
            while True:
                print(sec, end=' ')
                time.sleep(1)
                sec -= 1
                if sec == 0:
                    break

            print('\n''\033[92;1mЗЕЛЕНЫЙ\033[0m\n')
            time.sleep(1)
            sec = 7
            while True:
                print(sec, end=' ')
                time.sleep(1)
                sec -= 1
                if sec == 0:
                    break

a = TrafficLight()
a.running()

# 2.Реализовать класс Road (дорога). определить атрибуты: length (длина), width (ширина); значения атрибутов должны передаваться при создании экземпляра класса; атрибуты сделать защищёнными; определить метод расчёта массы асфальта, необходимого для покрытия всей дороги; использовать формулу: длинаширинамасса асфальта для покрытия одного кв. метра дороги асфальтом, толщиной в 1 смчисло см толщины полотна; проверить работу метода. Например: 20 м5000 м25 кг5 см = 12500 т.

class Road:
    def __init__(self, length, width):
        self._length = length
        self._width = width
        self.weight = 25
        self.height = 5

    def asphalt_mass(self):
        asphalt_mass = self._length * self._width * self.weight * self.height / 1000
        print(
            f'{round(self._length)}м * {round(self._width)}м * {round(self.weight)}кг * {round(self.height)}см = {round(asphalt_mass)}т.')
        print(f'Масса асфальта для покрытия 1м2 дороги: {round(asphalt_mass)}т.')

r = Road(5000, 20)
r.asphalt_mass()

# 3. Реализовать базовый класс Worker (работник). определить атрибуты: name, surname, position (должность), income (доход); последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}; создать класс Position (должность) на базе класса Worker; в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учётом премии (get_total_income); проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить значения атрибутов, вызвать методы экземпляров.

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": int(wage), "bonus": int(bonus)}

class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income["wage"] + self._income["bonus"]

p = Position('Валентин', 'Стукало', 'Technologist', '52600', '20000')
print(f'Сотрудник: {p.get_full_name()}',
      '\n'f'Общий доход (оклад + премия): {p.get_total_income()} руб.')

# 4. Реализуйте базовый класс Car. у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда); опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar; добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля; для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости. Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат. Вызовите методы и покажите результат.

import os
os.system("color")
c = {
    'PURPLE': '\033[95m',
    'CYAN': '\033[96m',
    'RED': '\033[91m',
    'BOLD': '\033[1m',
    'UNDERLINE': '\033[4m',
    'END': '\033[0m'
}

class Car:
    def __init__(self, auto_speed, auto_color, auto_name, is_police=False):
        self.auto_name = auto_name
        self.auto_speed = auto_speed
        self.auto_color = auto_color
        self.is_police = is_police

    def go(self):
        return f'\nАвтомобиль {self.auto_name} начал движение'

    def stop(self):
        return f'\nАвтомобиль {self.auto_name} совершил остановку'

    def turn(self, direction):
        return f'\nАвтомобиль {self.auto_name} совершил поворот {direction}'

    def show_speed(self):
        return f'\nСкорость автомобиля {self.auto_name} составляет: {self.auto_speed} км/ч'

class TownCar(Car):
    def show_speed(self):
        if self.auto_speed > 60:
            return f'\nВнимание! Снижайте скорость! Камера на 60.\nВаша скорость: {self.auto_speed} км/ч'
        else:
            return f'Скорость движения автомобиля {self.auto_name} - в пределах нормы'

class SportCar(Car):
    pass

class WorkCar(Car):
    def show_speed(self):
        if self.auto_speed > 40:
            return f'\nВнимание! Снижайте скорость! Камера на 40.\nВаша скорость: {self.auto_speed} км/ч'
        else:
            return f'Скорость движения автомобиля {self.auto_name} - в пределах нормы'

class PoliceCar(Car):
    pass

town = TownCar(80, 'Циан', '\033[96;1;4mLada Vesta\033[0m', False)
print('\n1:\n' + town.go(), town.show_speed(), town.turn('налево'), town.turn('направо'), town.stop())
sport = SportCar(30, 'Баклажан', '\033[95;4mLada Priora\033[0m', False)
print('\n2:\n' + sport.go(), sport.show_speed(), sport.turn('налево'), sport.stop())
work = WorkCar(120, 'Черный', '\033[1;1mBMW 320i\033[0m', False)
print('\n3:\n' + work.go(), work.show_speed(), work.turn('направо'), work.stop())
police = PoliceCar(59, 'Красный', '\033[91;1;4mPorsche Cayenne\033[0m', False)
print('\n4:\n' + police.go(), police.show_speed(), police.turn('направо'), police.stop())

# 5.Реализовать класс Stationery. Определить в нем атрибут title и метод draw. Метод выводит сообщение “Запуск отрисовки.” Создать три дочерних класса Pen, Pencil, Handle. В каждом из классов реализовать переопределение метода draw. Для каждого из классов метод должен выводить уникальное сообщение. Создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'

class Pen(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Pencil(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'

class Handle(Stationery):
    def draw(self):
        return f'Запуск отрисовки {self.title}'

pen = Pen('ручкой. "Внимание!"' )
print(pen.draw())
pencil = Pencil('карандашем. "Внимание!"')
print(pencil.draw())
handle = Handle(' - прошёл успешно')
print(handle.draw())