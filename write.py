f=open("one.txt","w")
f.write("hello student\n")
f.write("welcome to python file handling\n")
f.write("learning is fun!\n")
f.close()



f=open("one.txt","w")
f.write("new content only.\n")
f.close()


f=open("one.txt","a")
f.write("this line is added at the end.\n")
f.close()

f=open("one.txt","w")
lines=["python programming\n",
       "file handling\n",
       "error handling\n",
       "exception handling\n"
       ]
f.writelines(lines)
f.close()
