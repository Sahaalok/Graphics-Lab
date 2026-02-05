import pygame
import sys
pygame.init()
W,H=1000,1000
screen = pygame.display.set_mode((W,H))
WHITE = (255,255,255)
BLACK = (0,0,0)
def circle(xc,yc,r):
    # xc = int(input("Enter the x coordinate of center of circle"))
    # yc = int(input("Enter the y coordinate of center of circle"))
    # r = int(input("Enter the radius of a circle"))
    x = 0
    y = r 
    p = 1-r
    while(x<y):
        screen.set_at((xc+x,yc+y),WHITE)
        screen.set_at((xc+x,yc-y),WHITE)
        screen.set_at((xc-x,yc-y),WHITE)
        screen.set_at((xc-x,yc+y),WHITE)
        screen.set_at((xc+y,yc+x),WHITE)
        screen.set_at((xc-y,yc+x),WHITE)
        screen.set_at((xc-y,yc-x),WHITE)
        screen.set_at((xc+y,yc-x),WHITE)
        x = x+1
        if(p<0):
            y = y
            p = p+2*x+1
        else:
            y = y-1
            p = p+2*x-2*y+1
def ellipse(xc,yc,rx,ry):

    # xc = int(input("Enter the x center of ellipse"))
    # yc = int(input("Enter the y center of ellipse"))
    # rx = int(input("Enter the major of ellipse"))
    # ry = int(input("Enter the minor of ellipse"))
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
        screen.set_at((xc+x,yc+y),WHITE)
        screen.set_at((xc+x,yc-y),WHITE)
        screen.set_at((xc-x,yc-y),WHITE)
        screen.set_at((xc-x,yc+y),WHITE)
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
        screen.set_at((xc+x,yc+y),WHITE)
        screen.set_at((xc+x,yc-y),WHITE)
        screen.set_at((xc-x,yc-y),WHITE)
        screen.set_at((xc-x,yc+y),WHITE)
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        ellipse(500,500,150,75)
        ellipse(500,500,200,100)
        ellipse(500,500,250,150)
        ellipse(500,500,300,200)
        ellipse(500,500,350,250)
        ellipse(500,500,400,300)
        ellipse(500,500,450,350)
        ellipse(500,500,500,400)

        circle(500,500,50)
        circle(500+150,500,20)
        circle(500-200,500,20)
        circle(500,500+150,20)
        circle(500-300,500,20)
        circle(500,500+250,20)
        circle(500+400,500,20)
        circle(500,500+350,20)
        circle(500-500,500,20)

        pygame.display.flip()
if __name__ == "__main__":
    main()