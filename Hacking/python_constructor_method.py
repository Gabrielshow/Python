#use of classes
#indept understanding/practical aspects of python language
class D(object):
    def __del__(self):
        print('deleted')
    

print(D)
print(D.__module__)

#constructor method
#__init__() method
#__new__()
#__del__() destructor method

class C(D):                  #class declaration
    def __init__(self):      # "constructor"
        print ('initialized')
    
    def __del__(self):        # call parent destructor
        print ('deleted')
        
c1 = C()                 # instantiation
#initialized
c2 = c1                  # create additional alias
c3 = c1                  # create a third alias
print (id(c1), id(c2), id(c3))