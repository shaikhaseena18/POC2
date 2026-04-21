class Parent1:
    def func1(self):
        print("parent1 func1")
    def func2(self):
        print("parent1 func2")
class Parent2:
    def func1(self):
        print("parent2 func1")
    def func2(self):
        print("parent func2")
class Child(Parent1, Parent2):
    def func1(self):
        print("child func1")
        Parent1.func1(self)
        Parent2.func1(self)
    def func2(self):
        print("child func2")
        Parent2.func1(self)
        Parent1.func1(self)
        