#print message
print("hello world")

#add two numbers
a=input("enter first number:")
b=input("enter second number:")
sum=int(a)+int(b)
print("sum=",sum)

#even or odd
num=int(input("enter a number"))
if num %2 ==0:
    print("even number")
else:
    print("odd number")

#check leap year
year = int(input("Enter a year: "))

if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
    print("Leap Year")
else:
    print("Not a Leap Year")

#print pi value
import math
print(math.pi)

#store and print constant value
PI = 3.14
print(PI)
MAX_VALUE = 100
print(MAX_VALUE)

#square of a number
num = int(input("Enter a number: "))
square = num * num
print("Square =", square)

#area of circle
radius = float(input("Enter the radius: "))
area = 3.14 * radius * radius
print("Area of circle =", area)

#check data type
x = 10
y = 3.14
z = "Hello"
a = True

print(type(x))
print(type(y))
print(type(z))
print(type(a))

#use math function
import math
num = 16
print("Square root:", math.sqrt(num))
print("Power:", math.pow(2, 3))
print("Pi value:", math.pi)
print("Ceil value:", math.ceil(4.3))
print("Floor value:", math.floor(4.7))


#find power 
base = int(input("Enter base: "))
exponent = int(input("Enter exponent: "))
result = pow(base, exponent)
print("Result =", result)


#check positive or negative 
num = int(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num < 0:
    print("Negative number")
else:
    print("Zero")

