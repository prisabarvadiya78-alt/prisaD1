#(1)print number  from 1 to 5
i=1
while i<=5:
    print(i)
    i=i+1

#(2)sum of numbers take user input  
n = int(input("Enter n: "))
s = 0
i = 1
while i <= n:
    s = s + i
    i = i + 1
print("Sum:", s)

#(3)print odd number between 1 and 20
i = 1
while i <= 20:
    print(i)
    i = i + 2
   
#(4)print table of 4
num=int(input("Enter number:"))
i=1
while i<=10:
    print(num,"x",i,"=",num*i)
    i=i+1

#(5)print reverse number like 5 ,4,3,2,1
i = 5
while i >= 1:
    print(i)
    i = i - 1    

#(6)print largest number in list
numbers = [10, 45, 67, 23, 89, 34]

i = 0
largest = numbers[0]
while i < len(numbers):
    if numbers[i] > largest:
        largest = numbers[i]
    i = i + 1
print("Largest number is:", largest)

#(7)print even number between 1 and 20
i = 2
while i <= 20:
    print(i)
    i = i + 2