def discriminant(a,b,c):
    d = b**2-(4*a*c)
    if d == 0 :
        return 1
    else:
        return 2
    
print(discriminant(1,1.4,0.49))