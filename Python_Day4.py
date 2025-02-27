# Array -------> List

# Syntax :

var=[10,20,45,12,56]
var1=["Mayukhjit","Debrup","XYZ"]
var3=[10, "Mayukhjit", True, 45.56, 'h']

print(var1)

for i in var:
    print(i)

# 1s index 0
# Last index length-1

var.append(12)
var.append(56)
var.append(96)
var.pop()
print(var.count(12))
var.remove(12)
var.remove(10)
var.insert(1,89)
print(var)
print(var[0])
print(var[2])

# Check in a list all the elements are prime or not, if prime print the element


print("____________________________")
List=[45,13,69,78,21,23]

for i in List:
    count=0
    for j in range(1, i+1):
        if i%j==0:
            count+=1
    if count==2:
        print(i)

# Take list , and make 2 separate list for even and odd elements

ListOfAll=[13,23,45,80,12,45]
EvenList=[]
OddList=[]

for i in ListOfAll:
    if i%2==0:
        EvenList.append(i)
    else:
        OddList.append(i)

print(EvenList)
print(OddList)

# Functions in Python

def CheckPalindrome(number):
    temp=number
    rev=0
    while temp>0:
        rev=(rev*10)+(temp%10)
        temp=temp//10
    # print(rev)
    if rev==number:
        return 1
    else:
        return 0


# Take a list and check the numbers are palindrome or not

ListOfNum=[121, 34, 55, 676, 243]

print(CheckPalindrome(121))
for i in ListOfNum:
    if CheckPalindrome(i)==1:
        print(i)

