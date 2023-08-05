#the self parameter must be the first parameter of the function
#It could be named anything
#examples include

class Person:
    #giving the first variable of a class method a different name
    #other than self
    def __init__(mysillyobject, name, age):
        mysillyobject.name = name
        mysillyobject.age = age
    
    #creating a class method that prints the name variable of the class
    def myfunc(abc):
        print("Hello my name is " + abc.name)
        
p1 = Person("John", 36)       #creating an instance of the class
p1.myfunc()                   #accessing its method