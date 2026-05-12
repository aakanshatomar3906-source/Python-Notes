# What do we use to store data in Python?
# list, tuple, set, dictionary
# list :- collection of items which are ordered and changeable. Allows duplicate members.
# tuple :- collection of items which are ordered and unchangeable. Allows duplicate members.
# set :- collection of items which are unordered and unindexed. No duplicate members.
# dictionary :- collection of items which are ordered and changeable. No duplicate members.


# list:-
'''
my_list = [1, 2, 3, 4, 5]
print(my_list)  # [1, 2, 3, 4, 5]
print(type(my_list))  # <class 'list'>
print(my_list[0])  # 1
print(my_list[1])  # 2
'''

'''
list=[1,2,3,'sam',True,[2,3,4,5,7,8,9]]
print(list[5][1])  # 3

# slicing :-

print(list[0:4:1])  # [1, 2, 3, 'sam']
print(list[0:6:2])  # [1, 3, True]
print(list[-1])  # [2,3,4,5,7,8,9]'''

'''
a=[1,2,3,4,5,5,6.7,8,9,10]
print(a[-7:-1:-2])
print(a[-7:-1:2])
print(a[-7:-1])'''

# some inbuilt functions of list:-
'''
1. len(a)
2. append(a)
3. insert(index, value)
4. remove(value)
5. pop(index)
6. clear()
7. index(value)
8. count(value)

'''

# Strings : text data in python is called string. It is a sequence of characters. It is immutable. It is ordered. It is enclosed in single quotes, double quotes or triple quotes.
'''
name='masai'
print(name[0]) # m
print(len(name)) # 5
print(name[0:5:1]) # masai
'''
# some inbuilt functions of string:-
'''
1. len(a)
2. upper()
3. lower()
4. title()
5. strip()
6. split()
7. join()
8. replace(old, new)
9. find(value)
'''
'''
print(name.split('a')) # ['m', 's', 'i']
print(name.split('s')) # ['ma', 'ai']
print(name.split("&")) # ['masai']
print(name.split(" ")) # ['masai']
print(name.replace('a', 'o')) # mosoi
print(name.find('s')) # 2
print(name.find('z')) # -1'''


'''name2="masai school"
print(name2.split(' ')) # ['masai', 'school']
print(name2.split('s')) # ['ma', 'ai ', 'chool']
print(name2.replace('s', 'z')) # mazaizchool
'''

# 1. update string using list and third variable
name='masai'
name2=[]
bag=' '

for i in name:
    name2.append(i)
print(name2) # ['m', 'a', 's', 'a', 'i']


# other way
'''
for i in range(len(name)):
    print(name2.append(name[i]))
print(name2) # ['m', 'a', 's', 'a', 'i']'''

name2[0]='N'
for i in range(len(name2)):
    bag=bag+name2[i]
print(bag) #  masai

# 2. using  third variable
name='masai'
output=''
for i in range(len(name)):
    if i==0:
        output=output+'N'
    else:
        output=output+name[i]
print(output) 