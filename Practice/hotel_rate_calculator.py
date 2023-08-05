#Using default Arguments with Instantiation(hotel)
#Class definition for a fictitious hotel room rate calculator.
class HotelRoomCalc(object):
    'Hotel rooom rate calculator'
    
    def __init__(self, rt, sales = 0.085, rm = 0.1):
        '''HotelRoomCalc default arguments:
        sales tax == 8.5% and room tax == 10%'''
        self.salesTax = sales
        self.roomTax = rm
        self.roomRate = rt
    
    def CalcTotal(self, days = 1):
        'Calculate total; default to daily rate'
        daily = round((self.roomRate * (1 +self.roomTax + self.salesTax)), 2)
        return float(days) * daily

sfo = HotelRoomCalc(299)                     # new instance
print(sfo.CalcTotal())                       # daily rate
print(sfo.CalcTotal(2))                      # 2 day rate
sea = HotelRoomCalc(189, 0.086, 0.058)       # new instance
print(sea.CalcTotal())
print(sea.CalcTotal(4))
wasWKDay = HotelRoomCalc(169, 0.045, 0.02)   # new instance
print(sfo.__class__)                         # using an instance special attribute