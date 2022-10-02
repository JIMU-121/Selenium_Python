'''
city = "Delhi"

for c in city:
    print(c)
'''


'''
cities = [["india","Delhi"],["Australia","Melbourne"],["Canada","Vancouver"],["USA","New York"]]
for country,city in cities:
    print("County is "+country+" and city is "+city)
    
'''

cities = [["india","Delhi"],["Australia","Melbourne"],["Canada","Vancouver"],["USA","New York"]]

my_dictonary = dict(cities)
print(my_dictonary)

for country,city in my_dictonary.items():
    print(country,city)
    for s in country:
        print(s)

