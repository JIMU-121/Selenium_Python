
# max() Returns the largest item in an iterable
# min() Returns the smallest item in an iterable
# iter() Return an iterator object
# reversed() Return a reversed iterator
# next() Return the next item in an iterable
# slice() Return a slice object
# sorted() Return a sorted list
# sum() Sums the items of an iterator
# input() Allows User to input value

"""
demo_tuple = (5,7,8,4,5,6,1)
x = max(demo_tuple)
print(x)
"""

"""
demo_tuple = (5,7,8,4,5,6,1)
i = iter(demo_tuple)
j  = reversed(demo_tuple)
print(next(j))
print(next(j))
"""

demo_tuple = (5,7,8,4,5,6,1)
x = slice(2,5)
print(demo_tuple[x])

