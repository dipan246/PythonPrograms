class Parent:
    def __init__(self,name):
        self.father = name 

class Child(Parent):
    def __init__(self,son_name,father_name):
        super().__init__(father_name)
        self.son = son_name

    def display(self):
        print("I am {0} and my father is {1}".format(self.son,self.father))

a=Child('Divyanshu','Dipan')
a.display()

b=Child('Ram','Dasharatha')
b.display()
