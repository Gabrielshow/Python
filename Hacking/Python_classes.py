#implementation of switch case
#method 2
#using classes

class Python_Switch_implementation:
    def __init__ (self, number):
        self.number = number
    def day(self, number):
        def case_1(number):
            if number == 1:
                return 1
    
        def case_2(number):
            if number == 2:
                return 2
    
        def case_3(number):
            if number == 3:
                return 3
        
        def default(number):
            if number == 4:
                return 4
my_switch = Python_Switch_implementation(2)
my_switch.day(1)



    