def compute():
    LIMIT = 1000
    for a in range(1, LIMIT + 1):
        for b in range(a + 1, LIMIT + 1):
            c = LIMIT - a - b
            if a * a + b * b == c * c:
                temp_arr = [a, b, c]
                return str(a * b * c), temp_arr
    return None # Explicitly return None

#this function above could also be split into two more modular functions
# def calculate():
  # Compute a,b,c
    #LIMIT = 1000
    #for a in range(1, LIMIT + 1):
        #for b in range(a + 1, LIMIT + 1):
            #c = LIMIT - a - b
            #if a * a + b * b == c * c:
                #temp_arr = [a, b, c]
    #return a*b*c, temp_arr

#def compute():
  #results = calculate()
  #return str(results[0]), results[1]

#def main():
    #results = compute()
    #print1(*results)
    



def print1(a,b):
    print("The numbers are :")
    for c in b:
        print(c)
    print("and their product is", a)
    #this function returns an implicit NONE
    

def main():
    results = compute()
    print1(*results)
    

if __name__ == "__main__":
    print(main())
