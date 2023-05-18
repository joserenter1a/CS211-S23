"""
CS211 MT Review

Author: Jose Renteria
"""
line = '-' * 50


class People():
    def __init__(self, name):
        self.name = name

    def namePrint(self):
        print(self.name)


p1 = People("Sally")
p2 = People("Louise")

p1.namePrint()
print(line)


class A:
    def test(self):
        print('A.test')


class B(A):
    def test(self):
        print('B.test')
        super().test()


a_B = B()
a_B.test()
print(line)

"""
x = lib.A()
you know this is true, just like when you call
random.random() etc, you must specify the module
as the calling object, followed by the method
"""


class Canine():
    def __init__(self):
        pass


class Dog(Canine):
    def __init__(self):
        pass


print(Dog.__mro__[::])

print(line)


class Add:
    def __init__(self, x, y, z):
        self.sum = x + y + z


x = Add(1, 2, 3)
y = x.sum
# y is just a pointer to x.sum
x.sum = y + 1
# the same as x.sum += 1, using y as a reference
print(x.sum)
print(line)
"""
self is the current instance, aka calling object
or else the method would not know which object
to call the method upon
"""


class A:
    def m1(self):
        return self.m2()

    def m2(self):
        return 'A'


class B(A):
    def m2(self):
        return 'B'


a = A()
b = B()
print(a.m1(), b.m1(), a.m2(), b.m2())
# a.m2(), b.m2(), a.m2(), b.m2()
print(line)
a = 1
b = 1
index = 1
a_list = [1, 2, 3]

try:
    c = a / b
    print(a_list[index])
except IndexError as e:
    print("index out of range")
except ZeroDivisionError as z:
    print('b is 0')
"""
Assume it works, but handle cases where it doesn't
"""
print(line)
"""
pop returns a popped value at the specified index
so if it's empty, it has no index to pop from
"""
a = [1]
print(f'Popped value is {a.pop()}')
print(line)
"""
False:
cheer gets assigned to fun
"""


def fun(name):
    print(f'Hello {name}')


cheer = fun
# function aliasing
# create a new name for function fun
cheer('Geeks')
print(line)
"""
__init__() executes when a new object is instantiated

"""


class Foo: pass


class Bar(Foo): pass


print(f'Bar inherits from Foo')
print(Bar.__mro__[::])

print(line)
print(f'def __init__(self, title, author)')
print(f'Remember that you need a self, as the first param')
print(line)
"""
Yes, an abstract class can have both abstract and
non abstract subclasses
"""
x = [1, 2, 3]

x.append([4, 5, 6])
#x.extend([4,5,6])
# appends an element that is a list type
# extend would add the elements at the end
print(x, len(x))
print(line)

"""
An abstract class cannot be instantiated
"""
a, b, c = (2, 'apple', 3.5)
print('Tuple unpacking')
print((a, b, c))
print(line)
smpl = [1, 2, 3]
print(smpl)
#del(smpl)
# del will delete the whole object
smpl.pop()
print(smpl)
print(line)
"""
You can use a list to represent a stack
This is a very common usage
use pop for pop
append for push
[-1] for peek
It all depends on how you use it
~Polymorphism~
"""
print('list can be used to implement a stack')
print(line)


def sample_func():
    pass


print(f'When you print a function call\nYou print what it returns')
print(f'The return value from sample_func is {sample_func()}')
print(line)