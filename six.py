def equilateral_triangle(n):
    for i in range(n+1 ):
        for j in range( n - i ):
            print( " ", end = "")
        element = 1
        for k in range( 1, i+1 ):
            print(" ", element, end = "")
            element = element*(i - k)//(k)
        print()