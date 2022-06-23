from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name, age=0,h=0):
        self.name = name
        self.age = age
        self.h=h
    @abstractmethod
    def inf(self):
        pass
        # print('Animal name:  ', self.name)
        # print('Animal age:   ',self.age)
    def weight(self):
        print(self.h)
class Food(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def food(self):
        pass
        # print('Your food:  ')
class Breackfast(Food):

    def __init__(self):
      pass
    def food(self):
        print('EAT  ')
class Home_Animal(Animal,Food):
    def __init__(self,kind, name, age, weigt,h=2):
        super().__init__(name,age,h)
        super().inf()
        self.kind = kind
        self.weight=weigt
    def inf(self):
        print('The', self.kind, self.name,'have',self.age, 'ears old', 'and weight', self.weight,'kg')
    def __run(self):
        print('The', self.kind, self.name,'run')
    def food(self):
        print('EAT  ')
class Wild_Animal(Animal,Food):
    def __init__(self, name, age, kind,h):
        super().__init__(name,age,h)
        super().inf()
        self.kind=kind
    def inf(self):
        print('The',self.kind,self.name,'have',self.age,'ears old')
    def food(self):
        print('EAT  ')
home=Home_Animal('cat', 'Barsik',3,5,1)
# print(Wild_Animal.__dict__)
home.inf()
home.food()
home._Home_Animal__run()
Animal.weight(home)
wild=Wild_Animal('BIG',23,'Elephant',1)
wild.inf()
wild.food()
f=Breackfast()
f.food()