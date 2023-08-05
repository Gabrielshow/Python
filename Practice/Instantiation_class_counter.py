# by using a class variable to keep track
# of the number of instantiations of the class
class InstCt(object):
    count = 0              # count is class attr
    
    def __init__(self):    # increment count
        InstCt.count += 1
        
    def __del__(self):     # decrement count
        InstCt.count -= 1
        
    def howMany(self):      #return count
        return InstCt.count

a = InstCt()

b = InstCt()
print(b.howMany())
print(a.howMany())
del b
print(a.howMany())
del a
print(InstCt.count)
