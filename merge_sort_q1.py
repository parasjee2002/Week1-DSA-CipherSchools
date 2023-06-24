def mergeSortedArrays(a, m, b, n):
    i = m - 1
    j = n - 1
    k = m + n - 1

    while i >= 0 and j >= 0:
        if a[i] > b[j]:
            a[k] = a[i]
            i -= 1
        else:
            a[k] = b[j]
            j -= 1
        k -= 1

    while j >= 0:
        a[k] = b[j]
        j -= 1
        k -= 1

a = [1, 2, 3, 0, 0, 0]
b = [2, 5, 6]
m = 3
n = 3

mergeSortedArrays(a, m, b, n)

print("After merging:", a)
