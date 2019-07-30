n=int(input("Enter the entries:"))
t=[]
l=[]
for i in range(0,n):
    x=input("Enter the Time period,entries,entry/exit:")
    l.append(x.split(","))
t.append(l)
print(t)
for i in range(0,n):
    if(t[i][2]='entry'):
        income+=t[i][1]
    else:
        income-=t[i][l]
