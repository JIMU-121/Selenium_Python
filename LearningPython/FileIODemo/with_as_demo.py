# fw = open("demofile.txt", "w")
# fw.write("1st line")
# fw.close()

# fr = open("demofile.txt", "r")
# print(fr.read())
# fr.close()

with open("demofile.txt", "w") as fw:
    fw.write("This line is from with operation")

with open("demofile.txt", "r") as fr:
    print(fr.read())
