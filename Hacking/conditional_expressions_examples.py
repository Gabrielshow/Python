#additional python conveniences
if n>= 0:
    param = n
else:
    param = -n
result = foo(param)      #call the function

#using conditional expressions method 1
param = n if n >= 0 else -n #pick the appropriate value
result = foo(param)         #call the function

#using conditional expressions method 2
result = foo(n if n >= 0 else -n)
