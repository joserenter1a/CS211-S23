"""
Practice with matrices

Author: Jose Renteria
For CS211 Class Encore

MxN matrix
"""

class Matrix:
    def __init__(self):
        # TODO 
        pass # Remove before starting

        # Take input for the Rows and Columns

        # Initialize an empty list to hold the matrix values
        
        # Traverse M columns
            # inner list, remeber a matrix is a list of lists
            # Traverse N rows
                # Ask user for the values to be inputted into the matrix
                # append those values into our inner list
            # append the inner list to our matrix
        
    def __getitem__(self, i):
        # This is used for indexing/subscripting
        # TODO
        pass # Remove before starting
    
    def __str__(self):
        # str method for printing matrix with no brackets or formatting
        matrix_str = ''
        for row in self.matrix:
            matrix_str += ' '.join(map(str, row)) + '\n'
        return matrix_str

    def print_matrix(self):
        # going to print a row for each column, so that it looks *prettier*
        for k, el in enumerate(self.matrix):
            print(self.matrix[k])

    def search(self, target):
            return self.binary_search(target, 0, 0, self.M - 1, self.N - 1)
        
    def binary_search(self, target, start_row, start_col, end_row, end_col):
        # this cannot happen, check before you start
        if start_row > end_row or start_col > end_col:
            return None
        
        # middle formula, except you need to do it for both
        # row and col since you need the exact middle of the matrix
        mid_row = (start_row + end_row) // 2
        mid_col = (start_col + end_col) // 2
        # index at the middle value
        mid_value = self[mid_row][mid_col]
        
        # base case, if the middle is the target, return it
        if mid_value == target:
            return mid_row, mid_col
        # middle value greater than target, you know it is on the left
        elif mid_value > target:
            # recurse and move your end row pointer to the middle -1
            result = self.binary_search(target, start_row, start_col, mid_row - 1, end_col)
            # check if is not None
            if result is not None:
                return result
            else:
                # continue the recursion
                return self.binary_search(target, mid_row, start_col, end_row, mid_col - 1)
        else:
            # if not on the left, you know it is on the right
            # set your start pointer to the middle + 1
            result = self.binary_search(target, start_row, mid_col + 1, end_row, end_col)
            # check if is not None
            if result is not None:
                return result
            else:
                # continue the recursion
                return self.binary_search(target, mid_row + 1, start_col, end_row, mid_col)


    
if __name__ == '__main__':

    # just for printing clarity 
    line = ('~' * 50)

    # Matrix constructor
    matrix = Matrix()
    print(line)

    # Test usage, run this in the terminal, try the other matrix sizes 
    # python3 matrix_sol.py < matrixBIG.txt

    # formatted print
    matrix.print_matrix()
    print(line)

    # str print
    print(matrix)

    # Remember try except ?

    target = 54

    try:
        i, j = matrix.search(target)
        print(f'Target {target} found at index [{i}][{j}]')
    except:
        TypeError("cannot unpack non-iterable NoneType object")
        print(f'Target not found in matrix')
    