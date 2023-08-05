#iterators and Generators
#the most convenient method of creating iterators in Python is through the use of generators.
# a generator uses a yield statement to execute its values instead of directly returning them

#a regular function
def factors(n):                #traditional function that computes factors
    results = []               #store factors in a new list
    for k in range(1, n + 1):
        if n % k == 0:         #divides evenly, thus k is a factor
            results.append(k)  #add k to the list of factors
        return results         #return the entire list

#a generator
def factor(n):             #generator that computes factors
    for k in range(1, n + 1):
        if n % k == 0:     #divides evenly, thus k is a factor
            yield k        #yield this factor as next result
                
#more examples on generators
def factors(n):             #generator that computes factors
    k = 1
    while k * k < n:        #while k < sqrt(n)
        if n % k == 0:
            yield k
            yield n // k
        k += 1
    if k * k == n:         #special case if n is perfect square
        yield k
        
        
#using generators to generate an infinite series/ fibonacci series
def fibonacci():
    a = 0
    b = 1
    while True:             #keep going..
        yield a				#report value, a, during this pass
        future = a + b		
        a = b				#this will be next value reported
        b = future 			#and subsequently this