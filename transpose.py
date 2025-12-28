

r, c = map(int, input("Enter rows and columns of the matrix (r c): ").split())

print("Enter elements of the matrix:")
a = [[int(input()) for j in range(c)] for i in range(r)]

# Transpose logic
transpose = [[a[j][i] for j in range(r)] for i in range(c)]

print("\nTranspose of the matrix is:")
for i in range(c):
    for j in range(r):
        print(transpose[i][j], end=" ")
    print()
