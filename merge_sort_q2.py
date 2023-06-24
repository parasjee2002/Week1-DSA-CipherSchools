def firstOccurrence(nums, target):
    size = len(nums)
    start = 0
    last = size - 1
    index = -1
    while start <= last:
        mid = start + (last - start) // 2
        if nums[mid] == target:
            index = mid
            last = mid - 1
        elif nums[mid] > target:
            last = mid - 1
        else:
            start = mid + 1
    return index

def lastOccurrence(nums, target):
    size = len(nums)
    start = 0
    last = size - 1
    index = -1
    while start <= last:
        mid = start + (last - start) // 2
        if nums[mid] == target:
            index = mid
            start = mid + 1
        elif nums[mid] > target:
            last = mid - 1
        else:
            start = mid + 1
    return index

def searchRange(nums, target):
    firstOcc = firstOccurrence(nums, target)
    secondOcc = lastOccurrence(nums, target)
    return [firstOcc, secondOcc]

nums = [1, 2, 3, 4, 4, 4, 5, 6]
target = 4

result = searchRange(nums, target)

print("First Occurrence:", result[0])
print("Last Occurrence:", result[1])
