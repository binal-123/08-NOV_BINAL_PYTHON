import math
def susfacevolume(h,r):
    return(math.pi*r*r*h)  

def area(h,r):
    return((2*math.pi*r*h)+(2*math.pi*math pow(r,2)))


h=float(input('Enter height of cylinder:'))
r=float(input('Enter radius of cylinder:'))
vol=surfacevolume(h,r)
ar=area(h,r)
print('Surfacevolume:{0:2f}'.format(vol))
print('Area:{0:2f}'.format(ar))