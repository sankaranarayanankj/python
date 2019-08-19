n=int(input("Enter number:"))
k=1
for i in range(n,0,-1):
    for j in range(0,i):
        print(k,end=" ")
        k+=1
    print()
