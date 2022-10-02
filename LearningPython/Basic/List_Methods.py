
cities = ["Delhi","Mumbai","Melbourne","Sydney","Kolkata"]
print(cities)

# cities.append("lucknow")
cities.insert(1, "Lucknow")
cities.remove("Mumbai")
cities.pop(3)

print(cities.index('Delhi'))
cities.insert(1, "Lucknow")
print(cities.count("Lucknow"))
cities.sort()
print(cities)
cities.reverse()

print(cities)