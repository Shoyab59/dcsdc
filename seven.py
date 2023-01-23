def second_max_diff( arr ):
    max = float("-inf")
    s_max = float("-inf")

    min = float("inf")
    s_min = float("inf")
    
    for i in range(len(arr)):
        if(arr[i] > max):
            s_max = max
            max = arr[i]

        if(arr[i] < min):
            s_min = min
            min = arr[i]

    ans = max( s_max - min, max - s_min) # I figured that answer could be one of the combination of second-maximum and minimum or maximum and second-minimum
    return ans