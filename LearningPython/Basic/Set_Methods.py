
demo_set1 = {"Delhi","Kolkata","Melbourne","Sydney"}
demo_set2 = {"Delhi","Kolkata","Melbourne","Sydney","Lucknow","NewYork"}

'''
# Joning two Sets
# union()
# update()


#--Union will return a New Set
demo_set3 = demo_set1.union(demo_set2)
print(demo_set3)

#---Update will Update a Set
demo_set1.update(demo_set2)
print(demo_set1)

'''




'''
# keep Only Duplicates
# intersection()
# intersection_update()


demo_set3 = demo_set1.intersection(demo_set2)
print(demo_set3)

demo_set1.intersection_update(demo_set2)
print(demo_set3)
'''





'''
# keep all excluding duplicates
# symmetric_difference()
# symmetric_difference_update()

demo_set3 = demo_set1.symmetric_difference(demo_set2)
print(demo_set3)
demo_set1.symmetric_difference_update(demo_set2)
print(demo_set1)

'''





'''
# Return set containing difference between two or more sets
# difference()
# difference_update()

demo_set3 = demo_set2.difference(demo_set1)
print(demo_set3)
demo_set2.difference_update(demo_set1)
print(demo_set1)
'''





'''
# issubset()
# issuperset()

z = demo_set3 = demo_set1.issubset(demo_set2)
print(z)
z = demo_set2.issuperset(demo_set1)
print(z)

'''

