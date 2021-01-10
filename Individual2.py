#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Создать базовый класс Triad (тройка чисел) с операциями сложения с числом, умножения
# на число, проверки на равенство. Создать производный класс Vector3D, задаваемый
# тройкой координат. Должны быть реализованы: операция сложения векторов, скалярное
# произведение векторов

import math


class Triad:

    def __init__(self, A, B, C):
        self.__a = A
        self.__b = B
        self.__c = C

    def set_a(self, A):
        self.__a = A

    def get_a(self):
        return self.__a

    def set_b(self, B):
        self.__b = B

    def get_b(self):
        return self.__b

    def set_c(self, C):
        self.__c = C

    def get_c(self):
        return self.__c

    def get_coords(self):
        return self.get_a(), self.get_b(), self.get_c()

    def set_coords(self, A, B, C):
        self.__a = A
        self.__b = B
        self.__c = C

    def read(self, prompt=None):
        line = input() if prompt is None else input(prompt)
        parts = list(map(int, line.split(',')))

        for part in parts:
            if part == 0:
                raise ValueError()

        self.set_a(parts[0])
        self.set_b(parts[1])
        self.set_c(parts[2])

    def sum(self, A, B, C):
        self.__a += A
        self.__b += B
        self.__c += C
        return self.get_coords()

    def proiz(self, A, B, C):
        self.__a *= A
        self.__b *= B
        self.__c *= C
        return self.get_coords()

    def eq(self):
        if self.__a == self.__b == self.__c:
            return "Все 3 числа равны"
        if self.__a != self.__b or self.__a != self.__c or self.__b != self.__c:
            return "Числа не равны друг другу"


class Vector3D(Triad):
    def __init__(self, A=1, B=1, C=1):
        super(Vector3D, self).__init__(A, B, C)
        self.coords = self.get_coords()

    def read(self, prompt=None):
        Triad.read(self, prompt)
        return self.get_coords()

    def sum(self, A, B, C):
        Triad.sum(self, A, B, C)
        return self.get_coords()

    def proiz(self, A, B, C):
        Triad.proiz(self, A, B, C)
        return self.get_coords()


if __name__ == '__main__':
    print(((12 ** 2 + 12 + 3) % 20) + 1)
    Trd = Vector3D()
    Trd.read("Введите координаты 1 вектора ")
    vector2 = input("Введите коориднаты 2 вектора ").split(',')
    a = int(vector2[0])
    b = int(vector2[1])
    c = int(vector2[2])

    print("Координата при сложении векторов = {} "
          "Координата при умножении векторов (угол принят за 0) ={} ".format(Trd.sum(a, b, c), Trd.proiz(a, b, c)))
