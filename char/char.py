"""
Initialize a Character object class, implement functionality of all char methods

The char data type was designed to hold a single character .
A character can be a single letter, number, symbol, or whitespace

"""


class Char:
    def __init__(self, c: str):
        if len(c) != 1:
            return TypeError("Incorrect initialization of Char object")
        self.c = c

    def __str__(self):
        return f"{self.c}"

    def __repr__(self):
        return self.c

    def __add__(self, op):
        return self.c + op.c

    def __gt__(self, op):
        return self.c > op.c

    def __lt__(self, op):
        return self.c < op.c

    def __len__(self):
        return len(self.c)