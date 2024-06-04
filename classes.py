class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def speak(self,lang):
        print("hi my name is ",self.name, "and my age is",self.age,"and lang",lang)
manu = Person(name= "manaswini",age="20")
manu.speak("telugu")