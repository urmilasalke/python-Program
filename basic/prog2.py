#Question:
#Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5,
#between 2000 and 3200 (both included).
#The numbers obtained should be printed in a comma-separated sequence on a single line.

a=int(input("Enter starting number of  range in which you find the number divisible by 7 but not multiple of 5 "))
b=int(input("Enter ending  number of  range in which you find the number divisible by 7 but not multiple of 5 "))

for i in range(a,b):
    if i%7==0:
        if i%5!=0:
            print(i)




