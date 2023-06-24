def set_matrix_zeroes(matrix):
    n, m = len(matrix), len(matrix[0])
        
    row = set()
    col = set()
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                row.add(i)
                col.add(j)
                
    for i in row:
        for j in range(m):
            matrix[i][j] = 0
        
    for j in col:
        for i in range(n):
            matrix[i][j] = 0
    return matrix
matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(set_matrix_zeroes(matrix))