# Print all the even numbers between 1-100
range1=int(input("Enter Your Range : "))

for i in range(1, range1+1):
    if i % 2==0:
        print(i)

# Count no of vowels in String

UserString=input("Enter Your String : ")
counting=0
vowels="aeiouAEIOU"
for i in UserString:
    if i in vowels:
        counting=counting+1
print(f"your no of vowels are {counting}")



# Loop

for i in range(10):
    print(i)

for i in range(1, 10):
    print(i)

var="mayukhjit2001_"

for c in var:
    print(c)


# String Slicing

length=len(var)
print(length)
print(len("abcd123"))


print(var[2])
print(var[2:5])
print(var[2:])
print(var[:5])

# print(2+"4") this is not possible
print("Mayukhjit"+"Chakraborty")
print("2"+"5")
print(2+5)




age=int(input("Enter Your Age : "))

if age>18:
    print("Adult")
else:
    print("Not an Adult")

num=int(input("Enter My Number : "))

if num==0:
    print("It is a zero(neither Positive nor negative ")
elif num>0:
    print("Positive")
else:
    print("Negative")

# Take 3 numbers and determine the largest among those
num1=int(input("Enter Your 1st Number : "))
num2=int(input("Enter Your 2nd Number : "))
num3=int(input("Enter Your 3rd Number : "))

if num1>num2 and num1>num3:
    print(f"{num1} is greatest")
elif num2>num1 and num2>num3:
    print(f"{num2} is greatest")
else:
    print(f"{num3} is greatest")

# check You are Child , or Teenager or Adult

age=int(input("Enter Your age : "))

if age<13:
    print("You are Child")
elif age>=13 and age <=19:
    print("You are Teenager")
else:
    print("you are Adult")

# Check A character Vowel or not


alphabet=input("Enter Your Alphabet")

if alphabet=='a' or alphabet=='e' or alphabet=='i' or alphabet=='o' or alphabet=='u':
    print("Your Alphabet is vowel")
else:
    print("Your Alphabet is consonant")

vowel="aeiouAEIOU"
if alphabet in vowel:
    print(f"{alphabet} is vowel")

# Take a character check whether it is numeric, Alphabet or special

char=input("Enter Your Character : ")

if ('a'<=char<='z') or (char>='A' and char<='Z'):
    print("This is Alphabet")
elif char>='0' and char<='9':
    print("this is Numeric")
else:
    print("This is special")


# Take a number check whether it belongs to between 20 and 50 or not

number=int(input("Enter Your Number : "))


if number >= 20 and number<=50:
    print("it belongs to the given range")
else:
    print("it is outside from the range ")

