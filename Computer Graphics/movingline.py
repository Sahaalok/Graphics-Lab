import pygame
import sys
pygame.init()
W,H=800,600
screen = pygame.display.set_mode((W,H))
WHITE = (255,255,255)
BLACK = (0,0,0)
def translation(x1,y1,x2,y2):
    pygame.draw.line(screen,"RED",(x1,y1),(x2,y2),2)
    # tx = int(input("Enter the translation of x coordinate"))
    # ty = int(input("Enter the translation point of y coordinate"))
    for i in range (1,100):
        x = x1+i
        x3 = x2+i
        pygame.draw.line(screen,"GREEN",(x,y1),(x3,y2),2)
        pygame.display.flip()
        pygame.time.delay(100)
    
def main():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
                screen.fill(BLACK)
        translation(100,100,200,200)
        pygame.display.flip()
if __name__ == "__main__":
    main()