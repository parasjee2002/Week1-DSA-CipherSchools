def spiral_matrix(mat):
    r=len(mat)
    c=len(mat[0])
    m=[]
    # taking as nxn matrix 
    top=0
    right=c-1
    left=0
    bottom=r-1
    
    while(top<=bottom and left<=right):
        # i=right
        for i in range(left,right+1):
            # print(mat[top][i])
            m.append(mat[top][i])
        top+=1
        # j=top    
        for i in range(top,bottom+1):
            # print(mat[i][right])
            m.append(mat[i][right])
        right-=1
        # k=bottom
        if top<=bottom:
            # i=right
            for i in range(right,left-1,-1):
                # print(mat[bottom][i])
                m.append(mat[bottom][i])
            bottom-=1
        if left<=right:
            # i=bottom
            for i in range(bottom,top-1,-1):
                # print(mat[i][left])
                m.append(mat[i][left])
            left+=1
    return m
mat=[[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiral_matrix(mat))