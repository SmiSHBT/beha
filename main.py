1

class TriangleChecker:
    def __init__(self , a , b , c):
        self.a = a
        self.b = b
        self.c = c    
    try:
        def is_triangle(self):
            if self.a == self.b == self.c:
                print("Ура можно построить треугольник")
            elif self.a < 0:
                print("С отрицательными числами ничего не выйдет!")
            elif self.c < 0:
                print("С отрицательными числами ничего не выйдет!")
            elif self.b < 0:
                print("С отрицательными числами ничего не выйдет!")
            else:
                print("Жаль , но из этого не выйдет треугольник")
    except ValueError:
            print("Нужно вводить только числа!")

first = (input("vvedite 1 storonu: "))
second = (input("vvedite 2 storonu: "))
third = (input("vvedite 3 storonu: "))
TriangleChecker.is_triangle(first , second , third)

2

class Nikola:
    def __init__(self , name , age):
        self.name = name
        self.age = age
    try:
        def Nikolai(self):
            if self.name == "Nikolai" or self.name == "Николай":
                print(f"меня зовут {self.name} , мне {self.age} лет")
            elif self.name != "Nikolai" or self.name != "Николай":
                print(f"мое имя не {self.name} , мое имя Николай!")
    except ValueError:
        print('пиши нормально!')
a = input('vvedite imya: ')
b = int(input('vvedite skolko let: '))
Nikola.Nikolai(a , b)