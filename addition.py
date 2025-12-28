
r1, c1 = map(int, input("Enter r1, c1: ").split())
r2, c2 = map(int, input("Enter r2, c2: ").split())

if r1 == r2 and c1 == c2:
    print("Enter first matrix elements:")
    a = [[int(input()) for j in range(c1)] for i in range(r1)]

    print("Enter second matrix elements:")
    b = [[int(input()) for j in range(c2)] for i in range(r2)]

    c = [[a[i][j] + b[i][j] for j in range(c1)] for i in range(r1)]

    print("\nAddition of two matrices is:")
    for i in range(r1):
        for j in range(c1):
            print(c[i][j], end=" ")
        print()
else:
    print("Addition not possible (matrices have different sizes)")

