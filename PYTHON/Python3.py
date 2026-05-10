# LOOPS IN PYTHON :-
# ( INCREMENT AND DECREMENT )
# LOOP => USED TO EXECUTE STATEMENT OR EXPRESSIONS WHICH ARE REPATATIVE.
# 1. For Loop :-

'''
for i in range(1,11):
    print("hello",i)'''

'''
for i in range(5):
    print("hello")'''

'''
for i in range(1,11,2):
    print("hello",i)'''

'''
for i in range(1,10,3):
    print(i)  # 1,4,7'''

'''
for i in range(3,3):
    print(i)  # no output
'''



# 2. WHILE LOOP:-
'''
jump=0
while(jump<10):
    print("Jumping",jump)
    jump+=1'''
'''
jump=0
while(jump<10):
    jump+=1
    print("Jumping",jump)'''

'''
jump=0
while(jump<10):
    print("Jumping",jump)  # infinite loop
'''

'''
jump=100
while(jump>0):
    print("Jumping",jump)  # infinite loop
    jump-=1'''

'''
guest=1
while(guest<=10):
    if (guest==4):
        break
    print("Welcome Guest",guest)
    guest+=1'''

# while else:-
'''
i=1
while(i<6):
    print(i)
    i+=1
else:
    print("Loop is over")'''


'''
i=1
while i<10:
    i+=1
    if i==5:
        continue
    print(i)'''