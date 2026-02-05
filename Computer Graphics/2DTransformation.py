import math
import pygame
import sys
pygame.init()
W,H=800,600
screen = pygame.display.set_mode((W,H))
WHITE = (255,255,255)
BLACK = (0,0,0)
def translation(x1,y1,x2,y2,tx,ty):
    pygame.draw.line(screen,"RED",(x1,y1),(x2,y2),2)
    # tx = int(input("Enter the translation of x coordinate"))
    # ty = int(input("Enter the translation point of y coordinate"))
    x = x1+tx
    y = y1+ty
    x3 = x2+tx
    y3 = y2+ty

    pygame.draw.line(screen,"GREEN",(x,y),(x3,y3),4)
def scaling(x1,y1,x2,y2,sx,sy):
    pygame.draw.line(screen,"RED",(x1,y1),(x2,y2),2)
    # tx = int(input("Enter the translation of x coordinate"))
    # ty = int(input("Enter the translation point of y coordinate"))
    x = x1*sx
    y = y1*sy
    x3 = x2*sx
    y3 = y2*sy

    pygame.draw.line(screen,"GREEN",(x,y),(x3,y3),4)
def rotation(x1,y1,x2,y2,tx,ty,theta):
    pygame.draw.line(screen,"RED",(x1,y1),(x2,y2),2)
    # tx = int(input("Enter the translation of x coordinate"))
    # ty = int(input("Enter the translation point of y coordinate"))
    x = tx+(x1-tx)*math.cos(theta)-(y1-ty)*math.sin(theta)
    y = ty+(x1-tx)*math.sin(theta)-(y1-ty)*math.cos(theta)
    # x3 = x2+tx
    # y3 = y2+ty

    pygame.draw.line(screen,"GREEN",(x,y),(x2,y2),4)
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                screen.fill(BLACK)
        translation(100,100,200,200,125,125)
        scaling(100,100,200,200,2.2,2.2)
        rotation(100,100,200,200,125,125,90)
        pygame.display.flip()
if __name__ == "__main__":
    main()