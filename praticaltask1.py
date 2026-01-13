#calculate simple interest
p= float(input("Enter principal amount: "))
r = float(input("Enter rate of interest: "))
t = float(input("Enter time (in years): "))
simple_interest = (p * r* t) / 100
print("Simple Interest =", simple_interest)


#find maximum of 2 numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
if a > b:
    print("Maximum number is:", a)
else:
    print("Maximum number is:", b)


#print numbers  1 to 5
for i in range(1, 6):
    print(i)

#find length of a string
text = input("Enter a string: ")
length = len(text)
print("Length of the string:", length)


#print a welcome message
print("Welcome to Python Programming!")

#print 1st character of a string
text = input("Enter a string: ")
print("First character:", text[0])


#print last character of a string
text = input("Enter a string: ")
print("Last character:", text[-1])


#check postive or negative number
num = int(input("Enter a number: "))

if num > 0:
    print("Number is Positive")
elif num < 0:
    print("Number is Negative")
else:
    print("Number is Zero")


#add three numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
sum = a + b + c
print("Sum =", sum)


#take a input from any users
num = int(input("Enter a number: "))
print("Number is:", num)


