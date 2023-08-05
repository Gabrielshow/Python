#using copy.deepcopy() to duplicate a List
import copy
spam = [0,1,2,3,4,5]
cheese = copy.deepcopy(spam)
cheese[1] = 'Hello!'
print(spam)
print(cheese)