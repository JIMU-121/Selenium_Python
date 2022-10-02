
'''
Tuples are indexed, allow duplicate values and cannot
 be modified (immutable)
'''

demo_tuple = (1,2,3,4,5,6)
demo_tuple1 = ("Delhi","Mumbai","New York","Melbourne","Sydney")
demo_tuple2 = (True,False,False,True)
demo_tuple3 = (True,1,"Delhi",23.56)

print(demo_tuple1[1])
print(len(demo_tuple1[1]))

# Methods in Tuple
print(demo_tuple.count("Delhi"))
print(demo_tuple1.index("New York"))

for x in demo_tuple1:
    print(x)

joined_tuple = demo_tuple1 + demo_tuple2 + demo_tuple3
print(joined_tuple)
print(type(joined_tuple))
