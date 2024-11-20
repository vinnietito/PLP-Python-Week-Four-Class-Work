# f1 = open("myDataFile.txt", "r")

# print(f1)

f1 = open("myDataFile.txt", "r")
content = f1.read()
print(content)
f1.close()
