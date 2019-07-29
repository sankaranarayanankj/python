def firstnum(i):
    while i>10:  
        i=i//10
    return i
n=int(input("Enter number:"))
l=[]
l1=[]
d={}
w={}
str1=' '
print("Enter list of numbers:")
for i in range(0,n):
    x=int(input())
    l.append(x)
for i in l:
    x=firstnum(i)
    l1.append(x)
d=dict(zip(l,l1))
w=sorted(d.items(),key=lambda x:x[1],reverse=True)
for i in range(0,n):
    str1=str1+str(w[i][0])
print(str1)

