def print_Prime(n1:int,n2:int):
    for i in range(n1,n2+1):
        fact=0
        for j in range(1,i+1):
            if i%j==0:
                fact+=1
        if fact==2:
            print(i)

print_Prime(5,13)