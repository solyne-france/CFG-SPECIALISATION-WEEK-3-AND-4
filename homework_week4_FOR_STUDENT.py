"""
SEARCH IN MATRIX
--------

You are give a matrix (a list of lists) of DISTINCT integers and a target number.
Each row in the matrix is SORTED and each column in the matrix is SORTED.
Our matrix does not necessarily have the same height and width.

Write a function that returns a list of the row and column indices of the target integer
IF it is contained in the matrix, otherwise return [-1, -1].

EXAMPLE INPUT

matrix = [
[1,4,7,12,15,1000],
[2,5,19,31,32,1001],
[3,8,24,33,35,1002],
[40,41,42,44,45,1003],
[99,100,103,106,128,1004]
]

target =44

EXAMPLE OUTPUT

result = [3,3]

"""


#def search_in_matrix(matrix, target):
  #  pass
example_matrix = [
    [1, 4, 7, 12, 15, 1000],
    [2, 5, 19, 31, 32, 1001],
    [3, 8, 24, 33, 35, 1002],
    [40, 41, 42, 44, 45, 1003],
    [99, 100, 103, 106, 128, 1004]
]

example_target = 44


def search_in_matrix(matrix, target):
    row = 0
    col = len(matrix[0]) - 1

    while row < len(matrix) and col >= 0:
        if matrix[row][col] == target:
            return [row, col]
        if matrix[row][col] > target:
            col -= 1
        else:
            row += 1

    return [-1, -1]



def search_in_matrix1(matrix, target):
    row_idx = -1

    for lst in matrix:
        row_idx += 1
        col_idx = -1

        for num in lst:
            col_idx += 1

            if num == target:
                return [row_idx, col_idx]

    return [-1, -1]




def search_in_matrix2(matrix, target):
    for row_idx, lst in enumerate(matrix):
        for col_idx, num in enumerate(lst):
            if num == target:
                return [row_idx, col_idx]
    return [-1, -1]



def search_in_matrix3(matrix, target):
    if matrix[0][0] <= target <= matrix[-1][-1]:
        for row_idx, lst in enumerate(matrix):
            if lst[0] <= target <= lst[-1]:
                for col_idx, num in enumerate(lst):
                    if num == target:
                        return [row_idx, col_idx]
    return [-1, -1]




