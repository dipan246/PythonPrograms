class Parent:
    pass

class Child(Parent):
    def __init__(self,name):
        self.name = name

    def display(self):
        print("My name is: "+self.name)

a=Child('Divyanshu')
a.display()
