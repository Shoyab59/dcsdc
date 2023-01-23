def prod_eq( arr, value): # As in question it is mentioned to print only one pair
    for i in arr:
        Temp = value/i
        if(Temp in arr):
            return [i, Temp]
prod_eq( [1, 2, -3, 4, 5], -15)