#Question:
#Write a program that calculates and prints the value according to the given formula:
#Q = Square root of [(2 * C * D)/H]
#Following are the fixed values of C and H:
#C is 50. H is 30.
#D is the variable whose values should be input to your program in a comma-separated sequence.
#Example
#Let us assume the following comma separated input sequence is given to the program:
#100,150,180
#The output of the program should be:
#18,22,24

import math
c=50
h=30
d=[]
n=int(input("Enter value of n"))
for i in range(1,n+1):
    d.append(int(input()))

print(d)  
print(len(d))
print(type(d[0]))

for i in range(len(d)): 
    print(math.floor(math.sqrt((2*c*d[i])/30)))

