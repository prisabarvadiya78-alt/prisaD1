
f1=open("one.txt","r")
data1=f1.read()
f1.close()
f2=open("d1.txt","r")
data2=f2.read()
f2.close()
merged=open("merged.txt","w")
merged.write(data1)
merged.write("\n")
merged.write(data2)
merged.close()

print("file merged into merged.txt")
s