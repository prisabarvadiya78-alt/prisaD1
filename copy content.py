src=open("one.txt","r")
data=src.read()
src.close()


dst=open("D1.txt","w")
dst.write(data)
dst.close()
print("file copied successfully.")