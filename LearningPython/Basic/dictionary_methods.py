


demo_dict2 = {"qa":"testurl","uat":"uaturl","preprod":"preprodurl"}

print(demo_dict2.get("preprod"))

print(demo_dict2.keys())

print(demo_dict2.items())

print(demo_dict2.values())

print(demo_dict2.popitem())

demo_dict2.update({"prod":"produrl"})
demo_copy = demo_dict2.copy()

print(demo_dict2)
print(demo_copy)
demo_copy.clear()
print(demo_copy)

