n=int(input("Enter a number: "))
pointer1=int(n/2)
pointer2=int(n/2)
for i in range(0,n):
    for j in range (0, n):
        if(pointer1>=0 and pointer2<=n):
            if (j==pointer1 or j==pointer2):
                print("*",end="") 
            else: print(" ",end="")
    print()
    if(i<int(n/2)):
        pointer1-=1
        pointer2+=1
    else: 
        pointer1+=1
        pointer2-=1