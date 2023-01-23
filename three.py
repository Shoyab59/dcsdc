def last_count( arr ): # I Assumed there can be multiple ‘\n’ characters in the stream but we have to choose last ‘\n’ character according to question
    temp = ""
    for i in range(len(arr)):
        if( arr[i] == '\n'):
            temp = arr[i-1]
    
    if(temp == ""):
        return 0

    count = 0
    for j in arr:
        if(j == temp):
            count += 1
    return 0
 # If ‘\n’ is first and only one count of ‘\n’ in stream then answer is 0 as there is not any character before it.