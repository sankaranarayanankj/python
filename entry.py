n=int(input("Enter Entries:"))
l=[]
l1=[]
q=[]
l2=[]
p=[]
count=0
for i in range(0,n):
    x=input("Enter entry->")
    x=x.split(",")
    l.append(x)
#print(l[1][0])
for i in range(0,n):
    x=int(l[i][0])
    y=int(l[i][1])
    z=str(l[i][2])
    l1.append(x)
    l1.append(y)
    l1.append(z)
    q.append(l1)
    l1=[]
#print(q)
#print(l1)
for i in range(0,len(q)):
    if(q[i][2]=='entry'):
        count+=q[i][1]
    else:
        count-=q[i][1]
    l2.append(count)
print(l2)
w=max(l2)
if(l2[-1]!=0):
    print("This time period is invalid")
else:
    for i in range(0,len(l2)):
        if(w==l2[i]):
            print(i)
            break
for i in range(0,i,-1):
    if(q[i][2]=='Entry'):
        p.append(q[i][0])
print(p)

          
       
