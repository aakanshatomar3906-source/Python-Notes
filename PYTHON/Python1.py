# python = programming language .(WAY TO TALK TO COMPUTER).
# why python?
# 1. easy to learn and use. ( easy to read and write)
# 2. beginner friendly.
# 3. very powerful. ( used in many fields ( game, web, app, ai/ml))
# 4. free and open source.

# what can we do with python?
#1. web development ( django, flask)
# 2. data science ( pandas,numpy,matplotlib)
#3. machine learning(scikit-learn,tensorflow,keras)
#4. game development ( pygame)
#5. automation ( selenium, pyautogui)

print("hello world")

# this is a comment.
''' this is a multi line comment.'''


# 1. VARIABLE:=
# variable is a container that holds a value.

X=2
Name="python"
pi=3.14
print(X,Name,pi)

#2. DATA TYPES:
# int: whole numbers (1,2,3)
# float: decimal numbers (3.14, 2.5)
# str: text ("hello", "python")
# bool: true or false (True, False)


name='Alice' # string
age=30 # integer
is_student=True # boolean
weight=65.5 # float

print(type(name))
print(type(age))
print(type(is_student))
print(type(weight))

name,age,city='Alice',30,'New York'
print(f'MY name is {name}, I am {age} years old and I live in {city}.')

print("my name is " + name + ", I am " + str(age) + " years old and I live in " + city + ".")

print("my name is",name," I am",age,"years old and I live in",city)


a,b,c=10,20,30
print(a,b,c)


# create 3 string variables and print them in one line.
name,place,country='Bob','BHOPAL','INDIA'
print(name,place,country)

# swapping in python
x=3
y=2
x,y=y,x
print(x,y)


str1='hello'
str2='world'
print(str1 +' '+ str2)

num1='100'
num2=200
#print(num1+num2) # this will give an error because num1 is a string and num2 is an integer.
print(num1+str(num2))
print(int(num1)+num2)


# mathematics operations:-
# 1. addition (+)
# 2. subtraction (-)
# 3. multiplication (*)
# 4. division (/)

a=10
b=20
print(a+b) # addition
print(a-b) # subtraction
print(a*b) # multiplication
print(a/b) # division

print(10%3) # modulus ( gives the remainder)
print(2**3) # exponentiation ( gives the power)
print(10//3) # floor division ( gives the quotient without the remainder)
print(3**0.5) # square root ( gives the square root)

# Relational operators:-
# 1. greater than (>)
# 2. less than (<)
# 3. greater than or equal to (>=)
# 4. less than or equal to (<=)

x=10
y=20
print(x>y) # greater than
print(x<y) # less than
print(x>=y) # greater than or equal to
print(x<=y) # less than or equal to

# COMPARISON OPERATORS:-
# 1. equal to (==)
# 2. not equal to (!=)

X=50
Y=20
print(X==Y) # equal to
print(X!=Y) # not equal to

'''QUESTIONS:-'''
#1.
x=10
y=5
print(x+y)

name='Ravi'
print("hello "+ name)


a=8
b=2
print(a%b)

result=2**3
print(result)

is_coding_fun=True
print(type(is_coding_fun))

x=3
y=3.0
print(x==y)  # ?

