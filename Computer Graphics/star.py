import pygame
import sys
pygame.init()
W,H=800,600
screen = pygame.display.set_mode((W,H))
WHITE = (0,0,255)
BLACK = (255,255,255)
def BLA(x1,y1,x2,y2):

    # x1 = int(input("Enter the value of x1"))
    # x2 = int(input("Enter the value of x2"))
    # y1 = int(input("Enter the value of y1"))
    # y2 = int(input("Enter the value of y2"))
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    if(x2>x1):
        lx = 1
    else:
        lx = -1
    if(y2>y1):
        ly = 1
    else:
        ly = -1
    screen.set_at((round(x1),round(y1)),WHITE)
    x = x1
    y = y1
    if(dx>dy):
        pk = 2*dy-dx
        for k  in range (dx):
            if(pk<0):
                x = x+lx
                pk = pk+2*dy
            else:
                x = x+lx
                y = y+ly
                pk = pk+2*dy-2*dx
            screen.set_at((round(x),round(y)),WHITE)
    else:
        pk = 2*dx-dy
        for k in range (dy):
            if(pk<0):
                y = y+ly
                pk = pk+2*dx
            else:
                x = x+lx
                y = y+ly
                pk = pk+2*dx-2*dy
            screen.set_at((round(x),round(y)),WHITE)
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        screen.fill(BLACK)
        BLA(450,150,225,500)
        BLA(450,150,600,500)
        BLA(225,250,600,250)
        BLA(225,250,600,500)
        BLA(225,500,600,250)
        # BLA(350,550,350,450)
        # BLA(350,450,400,450)
        # BLA(400,450,400,550)
        # BLA(525,550,525,300)

        pygame.display.flip()
if __name__ == "__main__":
    main()