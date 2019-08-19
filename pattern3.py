n=int(input("Enter number:"))
k=65
l=1
x=0
for i in range(n,0,-1):
    x+=1
    for j in range(0,i):
        if(x%2==0):
            print(l,end=' ')
            l+=1
        else:
            print(chr(k),end=" ")
            k+=1
    k=65
    l=1        
    print()
