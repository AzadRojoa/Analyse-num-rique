def discriminant(a,b,c):
    d = (b*100)**2-(4*(a*100)*(c*100))
    if d/100 == 0 :
        return 1
    elif d > 0:
        return 2
    else:
        return 1
    
print(discriminant(1,1.4,0.49))