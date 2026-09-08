import math


class Fraction:
    def __init__(self, chislitel, znamenatel):
        if not isinstance(chislitel, int) or not isinstance(znamenatel, int):
            raise ValueError
        if znamenatel == 0:
            raise ValueError

        self.chislitel = chislitel
        self.znamenatel = znamenatel
        self.reduce()

    def reduce(self):
        nod = math.gcd(abs(self.chislitel), abs(self.znamenatel))
        self.chislitel //= nod
        self.znamenatel //= nod
        if self.znamenatel < 0:
            self.chislitel = -self.chislitel
            self.znamenatel = -self.znamenatel

    def read(self):
        self.chislitel = int(input("Введите числитель: "))
        self.znamenatel = int(input("Введите знаменатель: "))
        if self.znamenatel == 0:
            print("Ошибка: знаменатель не может быть равен нулю!")
            exit()
        self.reduce()

    def display(self):
        print("{}/{}".format(self.chislitel, self.znamenatel))

    # Сложение
    def __add__(self, other):
        c = self.chislitel * other.znamenatel + other.chislitel * self.znamenatel
        z = self.znamenatel * other.znamenatel
        return Fraction(c, z)

    # Вычитание
    def __sub__(self, other):
        c = self.chislitel * other.znamenatel - other.chislitel * self.znamenatel
        z = self.znamenatel * other.znamenatel
        return Fraction(c, z)

    # Умножение
    def __mul__(self, other):
        c = self.chislitel * other.chislitel
        z = self.znamenatel * other.znamenatel
        return Fraction(c, z)

    # Сравнения
    def __eq__(self, other):
        return self.chislitel * other.znamenatel == other.chislitel * self.znamenatel

    def __ne__(self, other):
        return not self.__eq__(other)

    def __lt__(self, other):
        return self.chislitel * other.znamenatel < other.chislitel * self.znamenatel

    def __gt__(self, other):
        return self.chislitel * other.znamenatel > other.chislitel * self.znamenatel

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

    def __ge__(self, other):
        return self.__gt__(other) or self.__eq__(other)


if __name__ == '__main__':
    f1 = Fraction(1, 2)
    f2 = Fraction(3, 4)

    print("f1 = ", end="")
    f1.display()
    print("f2 = ", end="")
    f2.display()

    print("Сложение (f1 + f2): ", end="")
    (f1 + f2).display()

    print("Вычитание (f1 - f2): ", end="")
    (f1 - f2).display()

    print("Умножение (f1 * f2): ", end="")
    (f1 * f2).display()

    print("f1 == f2: {}".format(f1 == f2))
    print("f1 != f2: {}".format(f1 != f2))
    print("f1 < f2: {}".format(f1 < f2))
    print("f1 > f2: {}".format(f1 > f2))
    print("f1 <= f2: {}".format(f1 <= f2))
    print("f1 >= f2: {}".format(f1 >= f2))

    f3 = Fraction(1, 1)
    f3.read()
    print("f3 = ", end="")
    f3.display()