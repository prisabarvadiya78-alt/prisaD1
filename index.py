#(1)positive indexing
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[0])
print(arr[2])
print(arr[4])

#(2)negative indexing
from array import array
arr=array('i',[10,20,30,40,50])
print(arr[-1])
print(arr[-2])
print(arr[-5])

#(3)empty array
from array import array
arr=array('i',[])
arr.append(10)
arr.append(20)
arr.append(30)
arr.append(40)
arr.append(50)
print(arr)



#(4)modifying element using index
from array import array
arr=array('i',[10,20,30,40,50])
arr[2]=35
print(arr)

#(5) give the value from user and print
from array import array
arr=array('i',[])
for i in range(5):
    n=int(input("enter number:"))
    arr.append(n)
    print("array elements are:")
    for i in arr:
        print(i)


#(6)index error
from array import array
arr=array('i',[10,20,30])
print(arr[5])
