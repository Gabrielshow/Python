#python doesn't have a switch statement
#alternative implementations of switch statement in python
#method 1

#dictionary mapping
def numbers_to_word(argument):
    switcher = {
        0 : 'Zero',
        1 : 'One',
        2 : 'Two'
        }
    return switcher[argument]

# if module is not imported then run from main
if __name__ == '__main__':
    argument = 0
    print(numbers_to_word(argument))
    