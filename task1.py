class Animal:
    name = 'default'
    hunger = 5

    def __init__ (self,name,hunger):
        self.name = input('Введите: ')
        self.hunger = hunger

class Cat(Animal):
    n = 1
    def meow(self,n):
        self.n = int(input('Введите количество: '))
a = Cat(1,2)
a.meow(1)
class Dog(Animal):
    n = 1
    def bark(self,n):
        self.n = int(input('Введите количество: '))
b = Dog(1,2)
b.bark(1)

while a.name == 'cat':
    if a.n > 5:
        print('Кот голодный! Meow', a.n, 'times')
        for x in range(5, a.n):
            user = input('Дайте еду: ')
            print('Meow')
        break
    else:
        print('Кошка поел')
        break
else:
    print('у нас нету такое животное')

while b.name == 'dog':
    if b.n > 5:
        print('Собака голодный! Bark', b.n, 'times')
        for x in range(5, b.n):
            user = input('Дайте еду: ')
            print('Bark')
        break
    else:
        print('Собака поел!')
        break
else:
    print('у нас нету такое животное')