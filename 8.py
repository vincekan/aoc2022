'''
Part 1
Idea is to check the 'view' from each cardinal direction, and log this in a logging matrix.
Zero values in this matrix represent invisible trees.

Define a function to check the views and updates the logging matrix, since this process is repeated per direction.
To get the input list (matrix) for this function, we can modify the input in place to save memory and run sequentially by:
1. Running through with no changes.
2. Reversing the row values in the list (matrix).
3. Transposing (and thereby turning cols into rows).
4. Reversing the row values in the transposed list (matrix).


Part 2
Just iterate through... 99x99 x4x99/2...
Function takes in current position and iterates in each direction.
Idea is to check the 'view' from each cardinal direction, and log this in a logging matrix.
Logging matrix keeps track of number viewed per direction.
Multiply out for each tree position at the end.

Part 2 definitely suboptimal. Can probably find some way to go through cell by cell and
discard as soon as a condition is met...
'''

def log_updater(log, mat, rows, cols):
    '''
    Takes in the logging matrix and current matrix as parameters.
    Iterates through the current matrix in a single direction.
    Returns the logging matrix with 1 if the tree is visible from that direction.

    :param log: List representing a matrix - logging
    :param mat: List representing a matrix - puzzle input
    :param rows: Integer dimension of matrix
    :param cols: Integer dimension of matrix
    :return: None - modifies log in place - probably bad form
    '''
    for row in range(rows):
        prev_val = 0 # Reset pre_val per row
        for col in range(cols):
            if int(mat[row][col]) > prev_val:
                prev_val = int(mat[row][col])
                log[row][col] += 1
            else:
                ...

def log_updater2(log, mat, rows, cols, dir):
    '''
    Takes in the logging matrix and current matrix as parameters.
    Iterates through the current matrix rows from left to right.
    Returns the logging matrix with number of visible trees from the cell, in that direction.

    :param log: List representing a matrix - logging
    :param mat: List representing a matrix - puzzle input
    :param rows: Integer dimension of matrix
    :param cols: Integer dimension of matrix
    :param dir: Integer representing direction, 0-3
    :return: None - modifies log in place - probably bad form
    '''
    for row in range(rows):
        for col in range(cols):                 # Iterates through each cell
            my_height = int(mat[row][col])      # Height of the tree at this cell
            max_height = 0                      # Log of the current tallest tree visible
            for tree in range(col+1, cols):     # Compares cells to the right
                curr_height = int(mat[row][tree])
                if curr_height >= my_height:    # You find a tree of same height or taller. Stop.
                    log[row][col][dir] += 1
                    break
                elif curr_height >= max_height:
                    max_height = curr_height
                    log[row][col][dir] += 1
                else:                           # Tree behind a taller tree. You can still see it! Increment.
                    log[row][col][dir] += 1


# Stream through file and process into list of integers
with open("8input.txt", "r") as myfile:
    lines = [list(line.strip()) for line in myfile]

# Get matrix dimensions n x m
n = len(lines)
m = len(lines[0])

# For Part 1:
# Make logging matrix of zeroes
log_mat = [[0 for col in range(m)] for row in range(n)]

# For Part 2:
# Instead of a single value, each cell has a list of values, one for each direction
log_mat2 = [[[0, 0, 0, 0] for col in range(m)] for row in range(n)]


# Take a single direction first.
log_updater(log_mat, lines, n, m)
log_updater2(log_mat2, lines, n, m, 0)

# Repeat this, with rows reversed, [::-1]
for row in range(n):
    log_mat[row] = log_mat[row][::-1]
    log_mat2[row] = log_mat2[row][::-1]
    lines[row] = lines[row][::-1]
log_updater(log_mat, lines, n, m)
log_updater2(log_mat2, lines, n, m, 1)

# Repeat this, with matrix transposed
log_mat = [[log_mat[j][i] for j in range(n)] for i in range(m)]
log_mat2 = [[log_mat2[j][i] for j in range(n)] for i in range(m)]
lines = [[lines[j][i] for j in range(n)] for i in range(m)]
log_updater(log_mat, lines, n, m)
log_updater2(log_mat2, lines, n, m, 2)


# Repeat this, with rows reversed again, [::-1]
for row in range(n):
    log_mat[row] = log_mat[row][::-1]
    log_mat2[row] = log_mat2[row][::-1]
    lines[row] = lines[row][::-1]
log_updater(log_mat, lines, n, m)
log_updater2(log_mat2, lines, n, m, 3)


# Part 1: Count the number of zeros in the logging matrix, and subtract from total nxm.
internal_zeroes = 0
for row in range(1, n-1):
    internal_zeroes += log_mat[row][1:-1].count(0)

# Total matrix, minus the perimeter (since some at the edge can be 0, which are not caught by the logging matrix)
print(n*m - internal_zeroes)

# Part 2: Iterate through the log matrix and find the maximum product.
max_prod = 0
for row in range(n):
    for col in range(m):
        curr_prod = 1
        for item in log_mat2[row][col]:
            curr_prod *= item
        max_prod = max(max_prod, curr_prod)

print(max_prod)
