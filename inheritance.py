class Animal:
    def __init__(self,n,t):
        self.name = n
        self.type = t
    
    def description(self):
        print("this is",self.name, "and it is",self.type,"this is")
class chimpu(Animal):
    def __init__(self,name,type,color):
        super().__init__(name,type)
        self.color = color
    def description(self):
        print("this is",self.name, "and it is",self.type)
        

d=Animal("dog","teritorial")


c=chimpu("chimpu","teritorial","black")
print(c.name)

c.description()

        