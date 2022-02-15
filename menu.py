
import pygame
import sys

WINDOW_WIDTH = 900
WINDOW_HEIGHT = 900
PURPLE = (70, 0, 150)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
mouseGridPos = [0, 0]
tituloPos = [0, 0]
pygame.init()
SCREENMenu = pygame.display.set_mode((WINDOW_HEIGHT, WINDOW_WIDTH))
def menuPrincipal():
    pygame.display.set_caption("Menu")
    clock = pygame.time.Clock()
    pygame.display.update()
    while True:
        mouse = pygame.mouse.get_pos()
        clock.tick(60) 
        pintarFondo(mouse)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    
def pintarFondo(mouseFondo): 
    blockSize = 60  # Set the size of the grid block
    SCREENMenu.fill(BLACK)
    for y in range(0, WINDOW_WIDTH, blockSize):
        for x in range(0, WINDOW_HEIGHT, blockSize):
            if x == tituloPos[0] and y == tituloPos[1]:
                rect = pygame.Rect(x, y, blockSize * 3, blockSize * 3)
                pygame.draw.rect(SCREENMenu, BLACK, rect)
                y = y * 3
            else:
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(SCREENMenu, PURPLE, rect, 4)
            
    pygame.display.update()
    

    
menuPrincipal()
