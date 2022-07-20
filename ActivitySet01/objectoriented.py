from _typeshed import SupportsNext
import sre_constants
from unicodedata import name


class _318:
    bench=100
    monitor=1
    def learn(self):
        print("hi python")
a=_318()
e=_318()
print(e.bench)
print(e.monitor)
e.learn()
print(a.bench)
a.learn()
print(_318.bench)
print(_318.learn)
#2nd example
class Myclass:
    '''this is my second class'''#doc
    a=10
    def func(self):
        print("Hi CSE")
print(Myclass.__doc__)
print(Myclass.a)
print(Myclass.func)
class student:
    def __init__(self,srn,name):
      self.srn=srn
      self.name=name
    def display(self):
        print("My name is {0} and srn is {1}".format(self.name,self.srn))
s1=student("R21EF220","GODHA")
s1.name="bheema"
del s1.srn
student.display(s1)
class computer: #encapsulation
    def __init__(self):
        self.__maxprice=100
    def sell(self):
        print("max price=", self.__maxprice)#__maxprice-private member
    def setprice(self,price):
        self.__maxprice=price
c1=computer()
c1.sell()
# cannot modify private member c1.__maxprice(1000)
c1.setprice(1000)
c1.sell()
class polygon:#abstraction
    def sides(self):
        pass
class triangle(polygon):
    def sides(self):
        print("triangle has 3 sides")
class pentagon(polygon):
    def sides(self):
        print("pentagon has  sides")
t=triangle()
t.sides()
p=pentagon()
p.sides()
#inheritance
class User:
    def __init__(self,name):
        self.name=name
    def printname(self):
        print("Name =" +self.name)
class programmer(User):
    def __init__(self,name):
        self.name=name
    def display(self):
        print("Programming Pyhton")
u1=User("shiva")
u1.printname()
u2=programmer("supreeth")
u2.printname()
u2.display()
#polymorphism-same function but different behaviour
class Parrot:
    def fly(self):
        print("parrots can fly")
    def swim(self):
        print("parrots can't swin")
class Penguin:
    def fly(self):
        print("penguin cannot fly")
    def swim(self):
        print("penguin can swin")
#common interface
def flying_test(bird):
    bird.fly()
    bird.swim()
#instantiate objects
p=Parrot()
g=Penguin()
#passing the object
flying_test(p)
flying_test(g)
