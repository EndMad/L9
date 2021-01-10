#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать класс Time для работы со временем в формате «час:минута:секунда». Класс
# должен включать в себя не менее четырех функций инициализации: числами, строкой
# (например, «23:59:59»), секундами и временем. Обязательными операциями являются:
# вычисление разницы между двумя моментами времени в секундах, сложение времени и
# заданного количества секунд, вычитание из времени заданного количества секунд,
# сравнение моментов времени, перевод в секунды, перевод в минуты (с округлением до
# целой минуты)


class Time:

    def __init__(self):

        self.__hour = 0
        self.__minute = 0
        self.__second = 0

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split(':')))

        self.__hour = int(parts[0])
        self.__minute = int(parts[1])
        self.__second = int(parts[2])

    # Инициализация времени числами
    def get_time1(self):
        return self.__hour, self.__minute, self.__second

    # Инициализация времени строкой
    def get_time2(self):
        hour = str(self.__hour)
        minute = str(self.__minute)
        second = str(self.__second)
        return hour + ':' + minute + ':' + second

    # Инициализация времени секундами
    def get_time3(self):
        return self.__hour * 3600 + self.__minute * 60 + self.__second

    # Инициализация времени временем
    def get_time4(self):
        hour = str(self.__hour)
        minute = str(self.__minute)
        second = str(self.__second)
        return hour + ' часов ' + minute + ' минут ' + second + ' секунд'

    def set_hour(self, hour):
        self.__hour = hour

    def set_minute(self, minute):
        self.__minute = minute

    def set_second(self, second):
        self.__second = second

    def get_hour(self):
        return self.__hour

    def get_minute(self):
        return self.__minute

    def get_second(self):
        return self.__second

    def time_raz(self, time1):
        return abs(self.to_second(time1) - self.get_time3())

    def time_plus(self, second):
        second = int(second)
        return self.get_time3() + second

    def time_minus(self, second):
        second = int(second)
        return self.get_time3() - second

    def time_eq(self, time2):
        if self.get_time3() < self.to_second(time2):
            return "Введенное время больше исходного"

        if self.get_time3() == self.to_second(time):
            return "Они равны"

        if self.get_time3() > self.to_second(time):
            return "Введенное время меньше исходного"

    def to_second(self, time3):
        time = time3.split(':')
        hour = int(time[0])
        minute = int(time[1])
        second = int(time[2])
        return hour * 3600 + minute * 60 + second

    def to_minute(self, time4):
        return int(self.to_second(time4) / 60)

    def dispaly(self, time, second1, second2):
        print("Инициализация введенного времени: {}, {}, {}, {}.   "
              "Вычисление разницы между введенным времинем и исходным Raz. Raz={}.   "
              "Прибавление секунд к исходному времени - {}.   "
              "Вычитание секунд из исходного времени - {}.   "
              "Сравнение введенного времени и исходного - {}.   "
              "Введенное время в секундах = {}. "
              "Введенное время в минутах = {}".format(self.get_time1(), self.get_time2(),
                                                      self.get_time3(), self.get_time4(),
                                                      self.time_raz(time), self.time_plus(second1),
                                                      self.time_minus(second2), self.time_eq(time),
                                                      self.to_second(time), self.to_minute(time)
                                                      )
              )


if __name__ == '__main__':
    Time = Time()
    Time.read("Введите исходное время ")
    time = input("Введите другое время для операций (введенное время) ")
    second1 = input("Введите количество секунд которые следует прибавить к введенному времени ")
    second2 = input("Введите количество секунд которые следует отнять от введенного времени ")
    Time.dispaly(time, second1, second2, )
