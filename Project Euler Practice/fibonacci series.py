#A simple function that prints the even numbers of the fibonacci sequence:

def main():
    number = int(input("Enter the number of the fibonnacci numbers to sum"))
    sum_fib = fib(number)
    print("the sum of the numbers is %", sum_fib)
    
def fibmemo(num):
    cache = []
    if num in cache:
        return num
    else:
        cache.append(num)
        
def isEven(num):
    evenNum = []
    fibarraylength = len(num)
    for i in range(fibarraylength):
        if num % 2 == 0:
            evenNum.append(num)
        
        else:
            return "this fib number is not even"
    return evenNum
    
def fib(n):
    cache = []
    fibsum = 0
    if n <= 1:
        return 1
    else:
        fibsum = fib(n-1) + fib(n-2)
        fibmemo(fibsum)
        
# Function for nth fibonacci 
# number

  
def fibonacci(n):
    FibArray = [0, 1]    
    
    # Check is n is less 
    # than 0
    if n < 0:
        print("Incorrect input")
          
    # Check is n is less 
    # than len(FibArray)
    elif n < len(FibArray):
        return FibArray[n]
    else:        
        FibArray.append(fibonacci(n - 1) + fibonacci(n - 2))
        return FibArray[-1]

if __name__ == '__main__':
    main() 