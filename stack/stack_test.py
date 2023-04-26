import unittest, time
from stack import *


class TestStackReversal(unittest.TestCase):

    def test_stack_init(self):
        s = stack()
        assert str(s) == 'deque([])'

    def test_reverse_same(self):
        inp = "1111"
        assert inp == reverse_string(inp)

    def test_reverse_empty(self):
        inp = ""
        assert inp == reverse_string(inp)

    def test_reverse_avg(self):
        inp = "101010"
        assert reverse_string(inp) == "010101"

    def test_reverse_time(self):
        inp = "1" * 1000  # a thousand length str
        start = time.time()
        reverse_string(inp)
        end = time.time()
        assert (end - start) < .001  # should be easily less than 1 ms

    def test_loop(self):
        i = 100
        while i > 0:
            self.test_reverse_time()
            i -= 1
        # encapsulated test case, calls another test case for more rigorous test of time