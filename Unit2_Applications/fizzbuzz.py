import random
print ("How many numbers should the program go up to?")
user_input=input()
x=int(user_input)
loop=0    
for hops in range(x):
    loop=loop+1
    if loop %3 == 0 and loop%5 == 0:
        print ("fizzbuzz")
    elif loop%5 == 0:
        print ("buzz")
    elif loop %3 == 0:
        print("fizz")
    else:
        print(loop)
