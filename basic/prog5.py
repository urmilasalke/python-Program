#Question:
#With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
#Suppose the following input is supplied to the program:
#8
#Then, the output should be:
#{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

a=int(input("Enter any number to create dictonary"))
d={}
for i in range(1,a+1):
    key=i
    value=i*i
    d[key]=value

print('{', end=" ")
for key,value in d.items():
    print(key,":",value,end=", ")

print('}')