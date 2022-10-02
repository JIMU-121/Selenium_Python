

# f = open("D:\\BCA\\Writedemo.txt","w")
# f.write("This is first line ")
# f.close()

f = open("Writedemo.txt","w")
l = [65,78,989,877]
for items in l:
    f.write(str(items)+"\n")
f.close()