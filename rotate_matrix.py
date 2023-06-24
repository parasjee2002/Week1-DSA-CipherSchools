def rotateMatrix(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(i):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i] = matrix[i][::-1]

def printMatrix(matrix):
    n = len(matrix)
    
    for i in range(n):
        for j in range(n):
            print(matrix[i][j], end=" ")
        print()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
printMatrix(matrix)

rotateMatrix(matrix)

print("Rotated Matrix:")
printMatrix(matrix)
