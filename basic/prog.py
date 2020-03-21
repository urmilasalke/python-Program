text=input("Enter 4 digit binary  string seperated by comma ")
l=text.split(",")

q=[]

for i in range(len(l)):
    mod=int(l[i])%5
    if mod==0:
         q.append(int(l[i]))

print(q)

