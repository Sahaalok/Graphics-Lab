# def DDAline():

#     x1=int(input("Enter x1 coordinate"))
#     y1=int(input("Enter y1 coordinate"))
#     x2=int(input("Enter x2 coordinate"))
#     y2=int(input("Enter y2 coordinate"))
#     dx=abs(x2-x1)
#     dy=abs(y2-y1)   
#     if(dx>dy):
#         step=dx
#     else:
#         step=dy
#     xinc=dx/step
#     yinc=dy/step
#     x=x1
#     y=y1
#     while(x!=x2 and y!=y2):
#         x=x+xinc
#         y=y+yinc
#         print(x,y)
# DDAline()

import pygame
import sys
pygame.init()
W,H=800,600
screen = pygame.display.set_mode((W,H))
WHITE = (255,255,255)
BLACK = (0,0,0)
def DDAline(x1,y1,x2,y2):

    # x1=int(input("Enter x1 coordinate"))
    # y1=int(input("Enter y1 coordinate"))
    # x2=int(input("Enter x2 coordinate"))
    # y2=int(input("Enter y2 coordinate"))
    dx = (x2-x1)
    dy = (y2-y1)   
    if(abs(dx)>abs(dy)):
        step=abs(dx)
    else:
        step=abs(dy)
    xinc=dx/step
    yinc=dy/step
    x=x1
    y=y1
    for i in range (step):
        x=x+xinc
        y=y+yinc
        screen.set_at((round(x),round(y)),WHITE)
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        DDAline(350,100,525,300)
        DDAline(350,100,300,300)
        DDAline(300,300,525,300)
        DDAline(300,300,300,550)
        DDAline(300,550,525,550)
        DDAline(350,550,350,450)
        DDAline(350,450,400,450)
        DDAline(400,450,400,550)
        DDAline(525,550,525,300)

        pygame.display.flip()
if __name__ == "__main__":
    main()
