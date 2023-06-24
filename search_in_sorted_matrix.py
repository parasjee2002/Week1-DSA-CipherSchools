def searchInRotatedMatrix(matrix, target):
    m = len(matrix)
    n = len(matrix[0])
    left = 0
    right = m * n - 1
    
    while left <= right:
        mid = (left + right) // 2
        mid_element = matrix[mid // n][mid % n]
        
        if mid_element == target:
            return True
        elif mid_element < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

matrix = [
    [4, 5, 6, 7, 8, 9, 10, 1, 2, 3],
    [11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
    [21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
]

target = 14
result = searchInRotatedMatrix(matrix, target)
print("Found:", result)
