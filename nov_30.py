def LHS (a,b):
    return (a+b)**2
def RHS(a,b):
    return a**2+2*a*b+b**2
l=LHS(2,3)
r=RHS(2,3)
print('LHS={0} RHS={1}'.format(l,r))
