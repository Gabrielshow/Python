#Comprehension syntax
#method 1
[expression fo r value in iterable if condition]

#method 2
result = []
for value in iterable:
    if condition:
        result.append(expression)

#method 2 example 2
squares = []
for k in range(1, n + 1):
    squares.append(k*k)
    
#using method 1 we get
squares = [k*k for k in range(1, n + 1)]

factors = [k for k in range(1, n + 1) if n % k == 0]

#python supports similar comprehension syntaxes that respectively produce a set, generator m or dictionary.
[k*k for k in range(1, n + 1)]  #list comprehension
{k*k for k in range(1, n + 1)}  #set comprehension
(k*k for k in range(1, n + 1))  #generator comprehension
{ k : k*k for k in range(1, n + 1) } #dictionary comprehension

#generator comprehension example
total = sum(k*k for k in range(1, n + 1))   #stores the sum of the first n squares