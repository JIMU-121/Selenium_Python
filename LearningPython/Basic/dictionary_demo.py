
''' Dictionaries are used to store data in key:value paris. They are changeable'''




demo_dict = {}
demo_dict1 = {1:20,2:45,3:50,6:67}
demo_dict2 = {"qa":"testurl","url":"uaturl"}
demo_dict3 = {'qa':34,3:"uaturl"}

print(demo_dict2)
demo_dict2['prod'] = 'produrl'
demo_dict2[1] = 56
print(demo_dict2)
demo_dict2.pop(1)
print(demo_dict2)
demo_dict2.pop('url')
print(demo_dict2)
