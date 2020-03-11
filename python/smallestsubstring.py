x=list(input())
l,l1=[],[]
for i in range(len(x)):
    for j in range(i,len(x)):
        if(x[j] not in l ):
            l.append(x[j])
        else:
            break
    l1.append(l)
    l=[]
for i in l1:
    v=len(i)
    l.append(v)
print((max(l)))

