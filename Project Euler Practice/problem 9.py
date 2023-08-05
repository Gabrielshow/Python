def pythagorean_checker(a,b,c):
    pythagorean_boolean = False
    if (a*a + b*b == c*c):
        pythagorean_boolean = True
    return pythagorean_boolean

def condition(a,b,c):
    exact_boolean = False
    if (a + b + c == 1000):
        exact_boolean = True
    return exact_boolean

def output_numbers_products(arr):
    product = 1
    for c in range(len(arr) + 1):
        product *= int(c)
    return product

def set_of_threes(arr):
    number = 3
    for i in range(len(arr) - number + 1):
        temp_numbers =  arr[i : i + number]
        pyt_bool = pythagorean_checker(*temp_numbers)
        if pyt_bool:
            exact_bool = condition(*temp_numbers)
            if exact_bool:
                result = output_numbers_products(temp_numbers)
                return result
            else:
                return None
        else:
            return None
         
def loop_numbers():
    array = []
    for i in range(1, 10001):
        array.append(i)
    return array
    
def main():
    main_number = loop_numbers()
    final_answer = set_of_threes(main_number)
    print(final_answer)


if __name__ == "__main__":
    main()
        