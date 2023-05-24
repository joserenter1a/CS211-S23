"""
Practice with matrices

MxN
"""

M = int(input("Rows: "))
N = int(input("Columns: "))
matrix = []

for i in range(M):
    l = []
    for j in range(N):
        values = int(input())
        l.append(values)
    matrix.append(l)


print(matrix)

for k, el in enumerate(matrix):
    print(matrix[k])

print(matrix[0][0] and matrix[i][j])

"""
k element
1 element
2 element
4 element
5 element


"""


mult = matrix[0][j] * matrix[i][0]
print(mult)
