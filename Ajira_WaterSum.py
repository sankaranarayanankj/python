#Inputs
day=int(input())
y=int(input())
l,l1,l2,l3,l4,req,f1,t,t1,d=[],[],[],[],[],[],[],[],[],{}
totsum=0
for i in range(y):
    z=input().split(" ")
    l.append(z)
    d[z[0]]=z[2]
c=int(input())
for i in range(c):
    y=input().split("_")
    l1.append(y)
#seperation of fed
for i in range(c-1):
    for j in range(i+1,c):
        if(l1[i][-1]==l1[j][0]):
            l1[i].append(l1[j][1])
for i in range(len(l1)):
    if(l1[i][0]=='f' or l1[i][0]=='F'):
        l2.append(l1[i])
#Finding 1 day total
for i in range(len(l)):
    totsum+=int(l[i][2])
#Finding 2,..,n Days requirement
for j in range(1,day):
    for i in range(len(l)):
        sub=int(l[i][2])-int(l[i][1])
        if(sub<int(l[i][1])):
            req.append(l[i][0])
        if(sub<0):
            l[i][2]=d[l[i][0]]
        else:
            l[i][2]=sub
    if(req!=[]):
        l4.append(req)   
    req=[]
f=[]
#seperation of list
for i in range(len(l4)):
    for j in range(len(l4[i])):
        for k in range(len(l2)):
            if(l4[i][j] in l2[k]):
                m=l2[k].index(l4[i][j])
                b=l2[k][:m+1]
                f.append(b)
    f1.append(f)
    f=[]
for i in range(len(f1)):
    for j in range(len(f1[i])):
        for k in range(len(f1[i][j])):
            if(f1[i][j][k] not in t):
                t.append(f1[i][j][k])
    t1.append(t)
    t=[]
#Final Output
for i in range(len(t1)):
    for j in range(1,len(t1[i])):
        totsum+=int(d[t1[i][j]])
print(totsum)
