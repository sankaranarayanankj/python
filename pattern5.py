n=int(input("n="))
k=2*n-2
q=n
for i in range(n,0,-1):
    for j in range(0,k):
        print(end=" ")
    k=k-2
    for j in range(0,k):
        print(i,end=" ")
    print()
    
    
