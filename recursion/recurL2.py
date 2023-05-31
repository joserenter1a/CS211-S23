"""
Recursion Madness Level II
Author: Jose Renteria
for CS211 Class Encore

Find the max value in a matrix, recursively

This problem is slightly trickier, but definitely fair game,
as it combines two of the major concepts in this course, 
in 2D arrays or matrices and recursion

Reference
https://www.youtube.com/watch?v=_RaIpPQ5aP8&list=PLDV1Zeh2NRsCmu1lb9grUcljeYJtmgmYc&index=5

"""

# abstracts the recursive function in a helper
def find_matrix_max(matrix):
    return matrix_max(0, 0, matrix)

def matrix_max(rows, cols, m):
    if rows == len(m):
        return None, None
    if cols == len(m[rows]):
        return matrix_max(rows+1, 0, m)
    max_row, max_col = matrix_max(rows, cols + 1, m)
    if max_row == None:
        max_row, max_col = rows, cols
    if m[rows][cols] > m[max_row][max_col]:
        max_row, max_col = rows, cols 
    return max_row, max_col

def test_matrix_max():
    matrix = [[1,9,6], [8,3,7]]
    res = find_matrix_max(matrix)
    print(f'The max of the matrix can be found at {res}')

if __name__ == '__main__':
    test_matrix_max()