class circle:
    def radius(self,radius):
        r=radius

    def area(self,r):
        area=(3.14*r*r)
        print('THE AREA OF CIRCLE IS:',area)

    def peri(self,r):
        peri=(2*3.14*r)
        print('THE PERIMETER OF CIRCLE IS:',peri)

cl=circle()
radius=int(input('enter the radius'))
cl.area(radius)
cl.peri(radius)



