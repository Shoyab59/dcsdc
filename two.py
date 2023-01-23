def triplet_max( arr ):
    if( len(arr) < 3 ): # Handling the edge case
        return -1
    elif( len(arr) == 3 ):
        return arr[0]*arr[1]*arr[2]

    ans = float("-inf")
    for i in range( len(arr) - 2 ):
        for j in range( i+1, len(arr) - 1 ):
            for k in range( j+1, len(arr)):
                ans = max( arr[i]*arr[j]*arr[k], ans)
    return ans
