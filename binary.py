x=int(input("number:"))
y=bin(x)
print(y)
c1=[]
y1=[]
c=0
q=y[2::]
for i in q:
    c1.append(int(i))
print(c1)
for i in range(0,len(c1)):
    if(c1[i]==1):
        for j in range(1,len(c1)):
            if(c1[j]==1):
                break
            else:
                c=c+1
        y1.append(c)
    c=0
    i=i
print(y1)
