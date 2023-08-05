class Person:
    #initializing the class
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    #initializing the class method
    def myfunc(self):
        print("Hello my name is " + self.name)
        
p1 = Person("John", 36)  #creating an instance of the class
p1.myfunc()              #calling the instance's method

