# CONDITIONAL STATEMENTS:-

#1. if statement
'''if True:
    print("THIS IS TRUE") '''

'''if (5>3):
    print("5 is greater than 3")
'''

# Q:- Check whether 2 numbers are equal or not.
'''a=2
b=3
if a==b:
    print("a and b are equal")'''

'''a=2
b=3
x=a==b
if x:
    print("a and b are equal")'''

#2.  if else
'''a=3
b=2
if (a==b):
    print("a and b are equal")
else:
    print("a and b are not equal")'''

# discount example 
'''total_bill=1000
discount_price_start=899
if total_bill>discount_price_start:
    print("you are eligible for discount")
else:
    print("you are not eligible for discount")'''

#3.  if elif else
'''total_bill=799
if(total_bill>500):
    print("10 % discount")
elif (total_bill>1000):
    print("20 % discount")
else:
    print("you are not eligible for discount")'''

'''total_bill=1299
if (total_bill>1000):
    print("20 % discount")
elif (total_bill>500):
    print("10 % discount")
else:    print("you are not eligible for discount")
'''

'''rice_available=False
wheat_available=True
apple_available=True
if(rice_available):
    print("rice is available")
elif(wheat_available):
    print("wheat is available")
else:
    print("apple is available")'''

'''rice_available=True
wheat_available=True
apple_available=True
if(rice_available):
    print("rice is available")
if(wheat_available):
    print("wheat is available")
if(apple_available):
    print("apple is available")'''

#4.  nested if
'''gender="Female"
AGE=25
if(gender=="Female"):
    if(AGE>=18):
        print("You are eligible for voting")
    else:
        print("You are not eligible for voting")'''

'''gender="Male"
age=21
if(gender=="Male"):
    if(age==21):
       print("man can marry")
    else:
        print("man can't marry")
else:
    if(age>=18):
        print("female can marry")
    else:
        print("female can't marry")'''



# Question:-
# A=> GREATER, B=> GREATER OR BOTH ARE EQUAL?

'''A=int(input("Enter the value of A: "))
B=int(input("Enter the value of B: "))
if(A>B):
    print("A is greater than B")
elif (B>A):
    print("B is greater than A")
else:
    print("A and B are equal")'''


# LOGICAL OPERATORS:-
# 1. and
# 2. or
# 3. not

# AND
# a=True
# b=False
# print(a and b)

# a=True
# b=True
# print(a and b)

# a=5>3
# b=6>3
# print(a and b)

# if a:
#     if b:
#         print("both are true")


# if a:
#     if b:
#         print("both are true")
# if a and b:
#     print("both are true")
    


'''gender="Female"
age=21
if(gender=="male" and age>=21):
    print('man can marry')
elif ( gender=="Female" and age>=18):
    print("female can marry")'''


# OR OPERATOR:-
# a=True
# b=False
# print(a or b)

# a=False
# b=False
# print(a or b)


'''gender="female"
age=18
if(gender=="male" and age>=21) or (gender=="female" and age>=18):
    print(gender,": can get married")
else:
    print(gender,": can't get married")'''


# NOT OPERATOR:-
# a=True
# if not a:
#     print("hello")
# else:
#     print("bye")


# QUESTION:-
# 1
'''if False:
    print("hello")
print("world")'''

# 2
''' which of th following values will be treated
as False in python if statements?
a) "False"
b) None
c)1
d) -5'''

'''if "False":
    print("hello")

if None:
    print("hello")  # None is treated as False in python if statements.

if 1:
    print("hello")

if -5:
    print("hello")'''


# 3
'''name1="Rahul"
name2="Rahul"
if name1==name2:
    print("both names are same")'''

# 4
'''name1="Rahul"
name2="Rahul "
if name1==name2:
    print("both names are same")
else: print("both names are different")'''

# 5
'''which of the following is not a falsy value in python?
a) []
b) {}
c) " "       => True because it is a string with a space character.
d) 0     '''

# 6
'''age=21
if age>=18 and age<25:
    print("Young adult")
else:
    print("Not a young adult")'''


# 7
'''
username=""  # empty string is treated as False in python if statements.
if not username:
    print("Please enter a username")
else:
    print("Username accepted")'''

# 8
'''
username=" "  # string with a space character is treated as True in python if statements.
if not username:
    print("Please enter a username")
else:
    print("Username accepted")'''



