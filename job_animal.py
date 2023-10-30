'''
设计一个简单的动物园系统，
其中包含不同类型的动物（如狗、猫和鸟）。
每个动物都有自己的属性（如名字、年龄）和行为（如发出声音）
。使用封装、继承和多态来完成。
实例方法
实例属性
类属性
构造方法
封装
继承
多态
'''


class Animal:
    hair=True
    def __init__(self,name,age,walking_pattern):
        self.name = name
        self.age = age
        self.walking_pattern = walking_pattern

    def make_sound(self):
        pass

    def animal_walking_pattern(self):
        pass

class Dog(Animal):
    def __init__(self,name,age,walking_pattern):
        super().__init__(name,age,walking_pattern)

    def make_sound(self):
        print(f"{self.name}的叫声是汪汪")

    def animal_walking_pattern(self):
        print(f"{self.name}会{self.walking_pattern}")

class Cat(Animal):
    def __init__(self, name, age, walking_pattern):
        super().__init__(name, age, walking_pattern)

    def make_sound(self):
        print(f"{self.name}的叫声是喵喵")

    def animal_walking_pattern(self):
        print(f"{self.name}会{self.walking_pattern}")

    def eat(self):
        print(f"{self.name}会吃鱼")

class Bird(Animal):
    def __init__(self, name, age, walking_pattern):
        super().__init__(name, age, walking_pattern)

    def make_sound(self):
        print(f"{self.name}的叫声是叽叽咋咋")

    def animal_walking_pattern(self):
        print(f"{self.name}会{self.walking_pattern}")

    def eat(self):
        print(f"{self.name}会吃虫子")
class Person:

    def eat(self):
        print("人类什么物种都会吃")

class AnimalEat():

    def eat_fish(self,animal):
        if issubclass(animal.__class__,Animal):
            animal.eat()
        else:
            print("不是动物的属性习惯")



dog=Dog("dog1",2,"run")
cat=Cat("cat1",1,"run")
bird=Bird("bird1",2,"fly")
person=Person()
dog.make_sound()
dog.animal_walking_pattern()
cat.make_sound()
cat.animal_walking_pattern()
bird.make_sound()
bird.animal_walking_pattern()
print(bird.hair)
AnimalEat().eat_fish(cat)
AnimalEat().eat_fish(bird)
AnimalEat().eat_fish(person)