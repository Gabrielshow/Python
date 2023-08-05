class MyClass(object):
    'MyClass class definition'
    myVersion = '1.1'           #static data
def showMyVersion(self):        #method
          print (MyClass.myVersion)
          
#let's use the dir() and the __dict__ to see the class's attributes
          #using the dir() we have
dir(MyClass)
          
          
MyClass.__dict__