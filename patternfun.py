def printPatt(n:int):
    for i in range(1,n+1):
        for _ in range(1,i+1):
            print(i,end=" ")
        print()
printPatt(6)