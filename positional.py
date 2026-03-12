#(1) basic positional arguments
def add(a,b):
  print("a=",a)
  print("b=",b)
  return a+b
result=add(2,5)
print("sum=",result)


#(2) student information
def student_info(name,roll,marks):
   print("Name:",name)
   print("Roll NO:",roll)
   print("Marks:",marks)
student_info("Ravi",101,85)

#(3) simple interst
def simple_interest(p,r,n):
   si=(p*r*n)/100
   print("simple interest:",si)
simple_interest(10000,2,2)
simple_interest(50000,1.2,3)

#(4)area of circle
def ar_circle(r):
   a_circle=3.14*r*r
   print("area of circle:",a_circle)
ar_circle(1.5)
ar_circle(4)    

#(5) check number positive negative or zero
def check_value(no):
  if(no>0):
     print("positive")
  elif(no<0):
      print("negative")
  else:
     print("zero")
check_value(0)
check_value(90)
check_value(-15)            

#(6)odd or even
def odd_even(no):
   if(no%2==0):
      print(f"value{no} is even")
   else:
      print(f"value{no} is odd")  
odd_even(50)
odd_even(15)

#(7)arithmatic operation subtraction,
#multiplication and division
def addition(a,b):
   add=a+b
   print("addition of two values",add)
addition(50,10.5)
addition(100,200)   

