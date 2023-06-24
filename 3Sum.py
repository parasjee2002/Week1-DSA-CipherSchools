def threeSum(nums):
    n=len(nums)  
    if n<=2:
        return []
    result=set() 
    nums.sort()
    
    for i in range(n - 2):
        if (i == 0 or nums[i] > nums[i - 1]):
            j=i+1
            k=n-1
        # tr=sum-nums[i]
        while(j<k):
            add=nums[i]+nums[j]+nums[k]
            if(add==0):
                result.add((nums[i],nums[j],nums[k]))
                j+=1
                k-=1
            if add<0:
                j+=1
            if add>0:
                k-=1
    return result
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))
                