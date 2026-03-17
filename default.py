#(1) basic default argument
def greet(name,msg="Good Morning"):
    print("Hello",name +",",msg)
greet("Asha")
greet("Ravi","Good Evening")


#(2)power function
def power(num,exp=2):
    return num**exp
print(power(3))
print(power(3,3))
print(power(2,4))

#(3)multiple default arguments
def student_info(name,age=18,course="BCA"):
    print("Name:",name)
    print("Age:",age)
    print("course:",course)
student_info("Ravi")
student_info("Seema",20) 
student_info("Amit",19,"BSC IT")   