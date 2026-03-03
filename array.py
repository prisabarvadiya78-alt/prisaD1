#write compalsary 
from array import array

#(1)example:Integer array
arr=array('i',[10,20,30,40])
print(arr)
print(type(arr))

#(2)len()-Number of elements
arr=array('i',[10,20,30,40,50])
print(len(arr))

#(3)append(X)-add element at end
arr=array('i',[10,20,30])
arr.append(40)
print(arr)

#(4)insert(pos,x)-insert at position
arr=array('i',[10,20,40])
arr.insert(2,30)
print(arr)

#(5)remove(x)-remove first occurrence
arr=array('i',[10,20,30,20,40,20,20])
arr.remove(20)
print(arr)

#(6)pop()-remove and return last element
arr=array('i',[10,20,30,40])
x=arr.pop()
print("removed:",x)
print(arr)

#(7)index(x)-find index of element
arr=array('i',[10,20,30,40])
print(arr.index(30))

#(8)count(x)-count occurrence
arr=array('i',[10,20,30,20,40])
print(arr.count(20))

#(9)reverse()-remove array
arr=array('i',[10,20,30,40,50,60])
arr.reverse()
print(arr)