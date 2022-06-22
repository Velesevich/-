from abc import ABC, abstractmethod
class Animal(ABC):
    def __init__(self, name, age=0,h=0):
        self.name = name
        self.age = age
        self.h=h
    @abstractmethod
    def inf(self):
        print('Animal name:  ', self.name)
        print('Animal age:   ',self.age)
    def weight(self):
        print(self.h)
class Home_Animal(Animal):
    def __init__(self,kind, name, age, weigt,h=2):
        super().__init__(name,age,h)
        super().inf()
        self.kind = kind
        self.weight=weigt
    def inf(self):
        print('The', self.kind, self.name,'have',self.age, 'ears old', 'and weight', self.weight,'kg')
    def __run(self):
        print('The', self.kind, self.name,'run')
class Wild_Animal(Animal):
    def __init__(self, name, age, kind,h):
        super().__init__(name,age,h)
        super().inf()
        self.kind=kind
    def inf(self):
        print('The',self.kind,self.name,'have',self.age,'ears old')



home=Home_Animal('cat', 'Barsik',3,5,1)

print(Wild_Animal.__dict__)
home.inf()
home._Home_Animal__run()
Animal.weight(home)
wild=Wild_Animal('BIG',23,'Elephant',1)
wild.inf()
