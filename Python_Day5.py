# Problem 1

UserInput=input("Enter Your String : ")

Alphabet=False
Numeric=False
Special=False

for i in UserInput:
    if i.isalpha():
        Alphabet=True
    elif i.isdigit():
        Numeric=True
    else:
        Special=True

if Alphabet and Numeric and Special:
    print("All are Present")
elif Alphabet and Numeric:
    print("Only Alphabet and Numeric are present")
elif Alphabet and Special:
    print("Only Alphabet and Special are present")
elif Numeric and Special:
    print("Only Special and Numeric are present")
elif Numeric:
    print("Only Numerics are present")
elif Special:
    print("Only Special chars are present")
else:
    print("Only Alphabets are present")

# Problem 2

UserInput2=input("Enter Your String : ")

newString=""
store=""
for i in UserInput2:
    if i not in newString:
        newString=newString+i
        store = store + i + str(UserInput2.count(i))

print(store)


# Problem 3

UserInput3=input("Enter Your String : ")
vowels="AEIOUaeiou"
vowel=""
cons=""
for i in UserInput3:
    if i in vowels:
        vowel=vowel+i
    else:
        cons=cons+i

print(cons+vowel)