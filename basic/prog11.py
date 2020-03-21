#Question:
#Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
#Suppose the following input is supplied to the program:
#without,hello,bag,world
#Then, the output should be:
#bag,hello,without,world

a=input("Enter comma seperated words for sort")
x=a.split(",")
x.sort()

z=[2,4,1]
print(z.sort())
print(type(x))
print(x)



