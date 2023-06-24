def sort012(nums):
    p0 = 0
    p1 = 0
    p2 = len(nums) - 1
    while p1 <= p2:
        if nums[p1] == 0:
            nums[p0], nums[p1] = nums[p1], nums[p0]
            p0 += 1
            p1 += 1
        elif nums[p1] == 1:
            p1 += 1
        elif nums[p1] == 2:
            nums[p1], nums[p2] = nums[p2], nums[p1]
            p2 -= 1

nums = [2, 0, 2, 1, 1, 0]
sort012(nums)
print(nums)
