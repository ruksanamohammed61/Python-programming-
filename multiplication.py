

r1, c1 = map(int, input("Enter rows and columns of first matrix (r1 c1): ").split())
r2, c2 = map(int, input("Enter rows and columns of second matrix (r2 c2): ").split())

if c1 != r2:
    print("Multiplication not possible (columns of first matrix != rows of second matrix)")
else:
    print("Enter elements of first matrix:")
    a = [[int(input()) for j in range(c1)] for i in range(r1)]

    print("Enter elements of second matrix:")
    b = [[int(input()) for j in range(c2)] for i in range(r2)]

    # Initialize result matrix with zeros
    c = [[0 for j in range(c2)] for i in range(r1)]

    # Matrix multiplication logic
    for i in range(r1):
        for j in range(c2):
            for k in range(c1):
                c[i][j] += a[i][k] * b[k][j]

    print("\nResultant matrix after multiplication:")
    for i in range(r1):
        for j in range(c2):
            print(c[i][j], end=" ")
        print()
