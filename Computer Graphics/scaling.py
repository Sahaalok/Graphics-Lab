import pygame
import sys
pygame.init()
W,H=800,600
screen = pygame.display.set_mode((W,H))
WHITE = (255,255,255)
BLACK = (0,0,0)
def scaling(x1,y1,x2,y2,sx,sy):
    pygame.draw.line(screen,"RED",(x1,y1),(x2,y2),2)
    # tx = int(input("Enter the translation of x coordinate"))
    # ty = int(input("Enter the translation point of y coordinate"))
    x = x1*sx
    y = y1*sy
    x3 = x2*sx
    y3 = y2*sy

    pygame.draw.line(screen,"GREEN",(x,y),(x3,y3),4)
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                screen.fill(BLACK)
        
        pygame.display.flip()
if __name__ == "__main__":
    main()