for i in range(1, 5):
    for j in range(1, 6- i):
        print(" ", end=" ")
    for k in range(0, 2 * i - 1):
        print("*", end=" ")
    print()
for i in range(5,0,-1):
    for j in range(0,5-i):
        print(" ", end=" ")
    for k in range((2*i)-1):
        print("*", end=" ")
    print()