def ellipse():

    xc = int(input("Enter the x center of ellipse"))
    yc = int(input("Enter the y center of ellipse"))
    rx = int(input("Enter the major of ellipse"))
    ry = int(input("Enter the minor of ellipse"))
    x = 0
    y = ry
    #for region 1 initial decision parameter is
    p1 = ry*ry-rx*rx*ry+(1/4)*rx*rx
    while((2*ry*ry*x)<=(2*rx*rx*y)):

        if(p1<0):
            x = x+1
            y = y
            p1 = p1+2*ry*ry*x+ry*ry
        else:
            x = x+1
            y = y-1
            p1 = p1+2*ry*ry*x-2*rx*rx*y+ry*ry
        print(xc+x,yc+y)
        print(xc+x,yc-y)
        print(xc-x,yc-y)
        print(xc-x,yc+y)
    # for region 2,initial decision parameter is 
    p2 = ry*ry*(x+1/2)*(x+1/2)+rx*rx*(y-1)*(y-1)-rx*rx*ry*ry
    while(y!=0):

        if(p2>0):
            y = y-1
            x = x
            p2 = p2-2*rx*rx*y+rx*rx
        else:
            x = x+1
            y = y-1
            p2 = p2-2*rx*rx*y+2*ry*ry*x+rx*rx
        print(xc+x,yc+y)
        print(xc+x,yc-y)
        print(xc-x,yc-y)
        print(xc-x,yc+y)
ellipse()