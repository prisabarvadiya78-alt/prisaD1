# print message
print("hello world")

# add two numbers 
a=input("enter first number:")
b=input("enter second number")
sum=int(a)+int(b)
print("sum=",sum)

# even or odd 
num=int(input("enter a number:"))
if num %2 ==0:
    print("even number")
else:
     print("odd number")

# check leap year
def is_leap_year(year)
    # A year is a leap year if it is divisible by 4
    # but not divisible by 100, unless it is also divisible by 400
    if (year % 4 == 0)
        if (year % 100 == 0)
            if (year % 400 == 0):
                return True
            else:
                return False
        else
            return True
    else
        return False

# Example usage
year = int(input("Enter a year: "))
if is_leap_year(year):
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")
    
  #print pi value
  import math

print("The value of pi is:", math.pi)  

#store and print constant value.
# Define a constant
PI = 3.14159

# Print the constant
print("The value of PI is:", PI)

# square of a number 
number = 5
square = number ** 2
print("Square is:", square)

# area of circle
import math
radius = float(input("Enter the radius of the circle: "))

area = math.pi * radius ** 2
print(f"The area of the circle is: {area}")


# check data type
x = 42
print(type(x))  

y = 3.14
print(type(y))  

z = "Hello"
print(type(z))  

a = [1, 2, 3]
print(type(a))  


#use math function
import math

angle_rad = math.pi /4 
print("Sine of 45 degrees:", math.sin(angle_rad))
print("Square root of 25:", math.sqrt(25))
print("5 factorial:", math.factorial(5))


#find power
base = 2
exponent = 3
result = base ** exponent
print("Result:", result)  


#check  positive  or negative
# Input from user
num = float(input("Enter a number: "))

# Check if the number is positive, negative, or zero
if num > 0:
    print("The number is positive.")
elif num < 0:
    print("The number is negative.")
else:
    print("The number is zero.")