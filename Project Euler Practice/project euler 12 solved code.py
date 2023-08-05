#Triangle numbers
#work in progress
def Triangle_numbers():
    triangle_array =  []
    result = 0
    for i in range(8):
        result += i
        triangle_array.append(result)
    return triangle_array

def number_generator():
    numbers = []
    for i in range(1,101):
        numbers.append(i)
    return numbers

def check_divisors(array):
    count = 0
    numbers = number_generator()
    for c in array:
        for j in numbers:
            if j > c:
                break
            else:
                if c % j == 0:
                    count += 1
                       
    return count
    

def main():
    Seven_triangle_numbers = Triangle_numbers()
    divisor_count = check_divisors(Seven_triangle_numbers)
    print(divisor_count)

if __name__ == "__main__":
    main()
                    
                    
    
        