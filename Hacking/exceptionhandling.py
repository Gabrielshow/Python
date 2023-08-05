#catching an exception
try:
    ratio = x/y
except ZeroDivisionError:
    pass

try:
    fp = open('sample.txt')
except IOError as e:
    print('Unable to open the file:', e)
    
#handling two or more errors in the same way by using a single except statement
age = -1
while age <= 0:
    try:
        age = int(input('Enter your age in years:'))
        if age <= 0:
            print('Your age must be positive')
    except (ValueError, EOFError):
        print('Invalid response')

#or using two individual except clauses
age = -1
while age <= 0:
    try:
        age = int(input('Enter your age in years:'))
        if age <= 0:
            print('Your age must be positive')
    except ValueError:
        print('That is an invalid age specification')
    except EOFError:
        print('There was an unexpected error reading input.')
        raise #let's re-raise this exception