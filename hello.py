# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
x = 9; y = 10; z = 13
print (x + 11 + y + 19 + z*3)

None

varA = "abcd"; varB = 1234

if type(varA) == str or type(varB) == str:
    print ("string involved")

elif varA > varB:
    print ("bigger")

elif varA == varB:
    print ("equal")

else:
    # If none of the above conditions are true,
    # it must be the case that varA < varB
    print ("smaller")
    # End of code
''' '''

num = 5
if num > 2:
    print(num)
    num -= 1
print(num)
# 01

num = 0
while num <= 5:
    print(num)
    num += 1
    
print("Outside of loop")
print(num)
#02
numberOfLoops = 0
numberOfApples = 2
while numberOfLoops < 10:
    numberOfApples *= 2
    numberOfApples += numberOfLoops
    numberOfLoops -= 1
print("Number of apples: " + str(numberOfApples))
#03

num = 10
while num > 3:
    num -= 1
    print(num) 
#04
    
num = 10
while True:
    if num < 7:
        print('Breaking out of loop')
        break
    print(num)
    num -= 1
print('Outside of loop')

#05

num = 100
while not False:
    if num < 0:
        break
print('num is: ' + str(num)) 

#06

#07

#08

#09

#10    
