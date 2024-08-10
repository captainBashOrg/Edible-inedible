import ast


class Animal:
    alive = True  # живой или не живой
    fed = False  # голодный или сытый

    def __init__(self, name):
        self.name = name


    def eat(self, food): # Результат поедания
        if food.edible:
            print(f"{self.name} съел {food.name}")
            self.fed = True
            #print(f"{self.name} наелся")
        else:
            print(f"{self.name} не стал есть {food.name}")
            self.alive = False
            #print(f"{self.name} умер")

class Plant:
    def __init__(self, name):
        self.name = name
        self.edible = False  # съедобное \ не съедобное

# Определение классов-наследников для Animal
class Mammal(Animal):
    def __init__(self, name):
        super().__init__(name)

class Predator(Animal):
    def __init__(self, name):
        super().__init__(name)


# Определение классов-наследников для Plant
class Flower(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = False

class Fruit(Plant):
    def __init__(self, name):
        super().__init__(name)
        self.edible = True


print('Задача "Съедобное, несъедобное"')

#Выполняемый код(для проверки):
a1 = Predator('Волк с Уолл-Стрит')
a2 = Mammal('Хатико')
p1 = Flower('Цветик семицветик')
p2 = Fruit('Заводной апельсин')

print(a1.name)
print(p1.name)

print(a1.alive)
print(a2.fed)
a1.eat(p1) # Хищник пробует есть цветок
a2.eat(p2) # млекопитающее Хати ест фрукт апельсин
if a1.alive:
    print(f"{a1.name} жив")
else:
    print(f"{a1.name} умер")

if a2.fed:
    print(f"{a2.name} сыт")
else:
    print(f"{a2.name} голоден")