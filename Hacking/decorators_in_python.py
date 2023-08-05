# special instance attributes
# we have the __class__ attribute that shows from which class the instance was instantiated
# and the usual __dict__ attribute
# always modify a class attribute with the classname, not an instance.
# invoking unbound methods

#class EmplAddrBookEntry(AddrBookEntry):
#   'Employee address book entry class'
#    def __init__(self, nm, ph, em):
#       AddrBookEntry.__init_(self, nm, ph)
#       self.empid = id
#       self.email = em
        
#static method/ class method
#using some examples
class TestStaticMethod:
    def foo():
        print ('Calling static method foo()')
        
    foo = staticmethod(foo)

class TestClassMethod:
    def foot(cls):
        print('calling class method foo()')
        print('foo() is part of class:', cls.__name__)
        
    foot = classmethod(foot)
    
#all this above can be achieved by using decorators e.g.
class TestStaticMethod:
    @staticmethod
    def foo():
            print('calling static method foo()')
            
class TestClassMethod:
    @classmethod
    def foot(cls):
            print('calling class method foo()')
            print('foo() is part of class:', cls.__name__)

tsm = TestStaticMethod()
TestStaticMethod.foo()
tsm.foo()
tcm = TestClassMethod()
TestClassMethod.foot()
tcm.foot()
        