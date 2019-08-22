a=1
l=[]
l1=[]
l2=[]
q=[]
w=[]
z=[]
x2=[]
sum1=0
sum2=0
s=[]
d=[]
while(a==1):
    x=input("Enter time:")
    x=x.split(":")
    for i in x:
        l.append(int(i))
    l1.append(l)
    l=[]
    y=input("Enter 9 digit phone no:")
    l2.append(y)
    a=int(input("Do you want continue press 1 or Quit press 0--->"))
print(l1,"<Time and cost list>",l2)
for i in range(0,len(l2)):
    if(l1[i][1]<=5 and l1[i][2]<1):
        sum1=((l1[i][1]*60)+l1[i][2])*3
        q.append(sum1)
    else:
        sum2=(l1[i][1]+1)*150
        q.append(sum2)
print("price list--->",q)
for i in range(0,len(l2)):
    for j in range(i+1,len(l2)):
        if(l2[i]==l2[j]):
            sum=q[i]+q[j]
            z.append(sum)
            x2.append(l2[i])
print(z,"<Highest price>",x2)
print(x2,l2,sep="-------")
for i in range(len(l2)):
    if x2[0]!=l2[i]:
        s.append(l2[i])
        d.append(q[i])
print(s,"<last list>",d)
    
