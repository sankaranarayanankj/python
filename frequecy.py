n=input("Enter the string:")
l=[]
l1=[]
c=[]
sum1=0
if(n==""):
    print("Empty String")
else:
    for i in n:
        l.append(i)
        if(i not in l1):
            l1.append(i)
    for i in range(l):
        for j in range(l1):
            if(l1[i]==l[j]):
               sum1=sum1+1
        c.append(sum1)
        sum1=0
    print(c)
    x=max(c)
    y=min(c)
    print(x,y)
        
