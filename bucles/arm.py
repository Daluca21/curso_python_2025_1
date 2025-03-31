for a in range(10):
    for b in range(10):
        for c in range(10):
            a_cubo = a*a*a
            b_cubo = b*b*b
            c_cubo = c*c*c
            if a_cubo + b_cubo + c_cubo == a*100 + b*10 + c:
                print(a, b, c)
            


         