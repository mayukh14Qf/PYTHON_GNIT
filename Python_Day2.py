
# Data Types and Literals
var1=12
var2=54.55
var3='e'
var4='%'
var5=True
var6=False
var7="Mayukhjit Chakraborty"
var8='Mayukhjit1235760'

print(var8)
print(var4)
print(var5)

print(var2,var1,var7)

# 1ha="gagsj" (This is not applicable)
#  User Input

# UserInput=input("Enter your String : ")
# UserInput1=int(input("Enter Your Number  : ")) # Type Casting (Converting My String Into Integer)

# print(UserInput, UserInput1)

# Swap 2 Numbers With  3rd Variable
a=10
b=30
c=a  # c=10, b=30 , a=10
a=b  # a=30 , c=10 , b=30
b=c  # b=10, c=10 , a=30
print("My a is : ", a)
print("My b is : ", b)

# Swap 2 Numbers Without 3rd Variable

x=10
y=30
x=x+y  # x=40 , y=30
y=x-y  # y=10 , x=40
x=x-y  # x=30 , Y=10
print("My x is : ", x)
print("My y is : ", y)

# Important Second Way

x1=10
y1=30
x1=x1*y1  # x1=300 , y1=30
y1=x1/y1  # y1=10 , x1=300
x1=x1/y1  # x1=30 , Y1=10
print("My x1 is : ", x1)
print("My y1 is : ", y1)

# Python Special Trick

p=10
q=20
(p, q)=(q, p)
print("My p is : ", x1)
print("My q is : ", y1)

# Operator

num1=35
num2=4

add=num1+num2
sub=num1-num2
mul=num1*num2
div=num1/num2  # Actual Answer in float
re=num1 % num2  # Reminder
qu=num1//num2   # Quotient

print(add, sub, mul, div, re,qu)
print(10>10)
print(10<10)
print(10==10)
print(10>=10)
print(10<=10)
print(10!=10)

print(10>10 and 10>=10 and 10>=10)   # If all the conditions are true then it will give us true
print(10>10 or 10>=10)  # If any of the one conditions is true then it will give us true

# Positive or negative Number
number1=int(input("Enter A number : "))
if number1>0:
    print(number1, " is a positive Number ")
else:
    print(number1, "is Negative Number ")

# Even or odd number
number2=int(input("Enter A number : "))
if number2 % 2==0:
    print(number2, " is a even Number ")
else:
    print(number2, "is odd Number ")

# Print Last Digit of a Number
number3=int(input("Enter A number : "))
last_digit=number3%10
print(f"the last digit of {number3} is ", last_digit)

# Greater Among Two
if number1>number2:
    print(number1, " is greater between these")
else:
    print(number2, "is greater between these")

# Take 2 number , Print the greater last digit between those

FirstNumber=int(input("Enter the 1st number "))
SecondNumber=int(input("Enter the 2nd Number "))

LastDigitOfFirst=FirstNumber%10
LastDigitOfSecond=SecondNumber%10

if LastDigitOfFirst>LastDigitOfSecond:
    print(LastDigitOfFirst)
else:
    print(LastDigitOfSecond)
