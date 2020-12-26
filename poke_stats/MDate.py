import datetime as dt
import pandas as pd

class MDate(dt.datetime):
    '''A modified datetime that holds only Year and Month data'''

    def __init__(self, year, month, day):
        dt.datetime(year=year, month=month, day=1)

    def __str__(self):
        if self.month >= 10:
            return "{year}-{month}".format(year=self.year, month=self.month)
        else:
            return "{year}-0{month}".format(year=self.year, month=self.month)
             

    def __add__(self, number):
        '''
        An operator overload to add months to the MDate object
        '''
        if self.month + number > 12:
            return MDate(self.year + int(number / 12), self.month + (number % 12), 1)
        else: 
            return MDate(self.year, self.month + number, 1)

    def __eq__(self, other):
        '''
        Checks for equality between MDates. Equality is achieved if their month and year are equal
        '''
        return (self.year == other.year) & (self.month == other.month)

    def __ge__(self, other):
        return (self.year >= other.year) | ((self.year == other.year ) & (self.month >= other.month))



