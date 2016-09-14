__author__ = 'pridemai'

"""
This class represents a row in the CSV
"""
class Row:
    def __init__(self, amount, years, interest, value):
        self.amount = amount
        self.years =years
        self.interest = interest
        self.value = value

    def __str__(self):
        return ','.join([self.amount, self.years, self.interest, self.value])+"\n"
"""
This is our writer class
"""
class IOWriter:

    @classmethod
    def save_row(cls, row):
        open("history.csv", "a+").write(str(row))


