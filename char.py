import re
x=input()
l,l1=[],[]
c,v=0,0
z=""
for i in x:
    if(i.isdigit()):
        c=c+1
        if(c>1):
            l1.pop(-1)
            z=z+i
        else:
            z=i
        
        l1.append(z)
        v=0
    else:
        v=v+1
        if(v>1):
            l.pop(-1)
            m=m+i
        else:
            m=i
        l.append(m)
        c=0
    
    
print(l)
print(l1)
for i in range(len(l)):
    print(l[i]*int(l1[i]),end="")




