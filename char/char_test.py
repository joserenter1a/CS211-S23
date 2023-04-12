"""
A test suite for our Character class


"""

import unittest
from char import *


class TestCharMethods(unittest.TestCase):

    def test_init(self):
        c = Char('c')

    def test_str(self):
        c = Char('c')
        assert str(c) == 'c'

    def test_repr(self):
        c = Char('c')
        x = Char('x')
        [c, x]

    def test_add(self):
        c = Char('c')
        x = Char('x')
        assert c + x == 'cx'
        assert type(c + x) == str

    def test_gt(self):
        c = Char('c')
        x = Char('x')
        assert (c > x) == False
        assert (x > c) == True

    def test_lt(self):
        c = Char('c')
        x = Char('x')
        assert (c < x) == True
        assert (x < c) == False

    def test_len(self):
        c = Char('c')
        x = Char('x')
        assert len(c) and len(x) == 1
        assert len(c) - len(x) == 0
