"""
Initialize a Character object class, implement functionality of all char methods

The char data type was designed to hold a single character .
A character can be a single letter, number, symbol, or whitespace

"""


class Char:
    def __init__(_self, c: str):

        if len(c) != 1:
            return TypeError("Incorrect initialization of Char object")
        
        _self.c = c

    def __str__(_self):
        return f"{_self.c}"

    def __repr__(_self):
        return _self.c
    
    def __eq__(_self, other):
        return _self.c == other.c

    def __add__(_self, op):
        return _self.c + op.c

    def __gt__(_self, op):
        return _self.c > op.c

    def __lt__(_self, op):
        return _self.c < op.c

    def __len__(_self):
        return len(_self.c)