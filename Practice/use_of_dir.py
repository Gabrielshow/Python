class MyClass(object):
    'MyClass class definition'
    myVersion = '1.1'           #static data
def showMyVersion(self):        #method
    print (MyClass.myVersion)

myclass = MyClass
#let's use the dir() and the __dict__ to see the class's attributes
#using the dir() we have
#the dir() returns a list of (just the) names of an object's attributes
#while __dict__ is a dictionary whose attribute names are the keys and whose values are the data values of the corresponding attribute objects.
dir(MyClass)    
          
          
MyClass.__dict__

#special class attributes
#c.__name__   ---   String name of class c
#c.__doc__    ---   Documentation String for class c:
#c.__bases__  ---   Tuple of class c's parent classes
#c.__dict__   ---   Attributes of c
#c.__module__ ---   Module where c is defined (new in 1.5)


print(myclass.__name__)
print(myclass.__doc__)
print(myclass.__bases__)