n=int(input("Enter number:"))
k=1
t=0
for i in range(0,n+1):
    for j in range(0,i):
        print(k,end=" ")
        k+=1
        t+=1
    print()
for i in range(n+1,0,-1):
    for j in range(0,i):
        print(k,end=" ")
        k-=1
    print()
