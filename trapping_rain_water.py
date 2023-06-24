def trap(height):
    
    # two pointer approach
    size=len(height)
    left=0
    right=size-1
    left_max=height[left]
    right_max=height[right]
    result=0
    while(left<=right):
        if left_max<right_max:
            left_max=max(left_max,height[left])
            result+=left_max-height[left]
            left+=1
        else:
            right_max=max(right_max,height[right])
            result+=right_max-height[right]
            right-=1
    return result
height = [4,2,0,3,2,5]
print(height)