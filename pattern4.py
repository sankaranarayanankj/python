n=int(input("n="))
k=2*n-2
for i in range(0,n):
    for j in range(0,k):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    k=k-1
    print()
k=2
for i in range(n,-1,-1):
    for j in range(0,k):
        print(end=" ")
    for j in range(0,i+1):
        print("*",end=" ")
    k+=1
    print()
