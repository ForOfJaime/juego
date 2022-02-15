from asyncio import threads
from numbers import Integral
import random
import pygame
import sys
import numpy as np



BLACK = (0, 0, 0)
green = (10, 0, 50)
white = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

WINDOW_HEIGHT = 900
WINDOW_WIDTH = 900
bool_arr = np.array([False, False, False, False], dtype=bool)
position_site = [0, 0]

numeroGanador = 4
listaRoja = []
listaAmarilla = []
ultimaFichaTiradaRoja = [0, 0]
ultimaFichaTiradaAmarillo = [0, 0]
turnoTirador = False
def main():
    global SCREEN, CLOCK, turnoTirador
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    fpsCount1 = 0
    fpsCount2 = 0
    SCREEN.fill(BLACK)
    drawGrid()
    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(60)
    turnoTirador = bool(random.getrandbits(1))
    while True:
        clock.tick(60)
        fpsCount1 = fpsCount1 + 1
        fpsCount2 = fpsCount2 + 1
        print(fpsCount2)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                fpsCount1 = 0
                fpsCount2 = 0
                turnoTirador = lecturaFichas()
                get_input_arrows()
                drawGrid()
        if fpsCount1 >= 1:
            fichaDesciende()
            drawGrid()
            fpsCount1 = 0 
             
        if fpsCount2 >= 15:
            for i in range(0, 870, 60):
                for x in range(0, 870, 60):
                    comprobacionGanadorRojo([i, x])
                    comprobacionGanadorAmarillo([i, x])
            fpsCount2 = 0 
         

def drawGrid():
    blockSize = 60  # Set the size of the grid block
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            if x == position_site[0] and y == position_site[1]:
                rect = pygame.Rect(x, y, blockSize, blockSize)
                if turnoTirador == True:
                    pygame.draw.rect(SCREEN, RED, rect, 4)
                    pygame.draw.lines(SCREEN, green, True, [(x+90, y + 60),(x+90, y + 870)],1)
                    pygame.draw.lines(SCREEN, white, True, [(x+30, y + 60),(x+30, y + 870)],1)
                    pygame.draw.lines(SCREEN, green, True, [(x-30, y + 60),(x-30, y + 870)],1)
                else:
                    if turnoTirador == False:
                        pygame.draw.rect(SCREEN, YELLOW, rect, 4)
                        pygame.draw.lines(SCREEN, green, True, [(x+90, y + 60),(x+90, y + 870)],1)
                        pygame.draw.lines(SCREEN, white, True, [(x+30, y + 60),(x+30, y + 870)],1)
                        pygame.draw.lines(SCREEN, green, True, [(x-30, y + 60),(x-30, y + 870)],1)
            else:
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(SCREEN, green, rect, 4)

    blockSize = 60
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            for i in range(0, len(listaRoja), 1):
                if x == listaRoja[i][0] and y == listaRoja[i][1]:
                    rect = pygame.Rect(x, y, blockSize, blockSize)
                    pygame.draw.rect(SCREEN, RED, rect, 4)

            for i in range(0, len(listaAmarilla), 1):
                if x == listaAmarilla[i][0] and y == listaAmarilla[i][1]:
                    rect = pygame.Rect(x, y, blockSize, blockSize)
                    pygame.draw.rect(SCREEN, YELLOW, rect, 4)

    pygame.display.update()


def get_input_arrows():
    if (pygame.key.get_pressed()[pygame.K_a] == True) and position_site[0] != 0 and turnoTirador == True :
        position_site[0] = position_site[0] - 60
        
    if (pygame.key.get_pressed()[pygame.K_i] == True) and position_site[0] != 0 and turnoTirador == False:
        position_site[0] = position_site[0] - 60
        
    if(pygame.key.get_pressed()[pygame.K_d] == True) and position_site[0] != 840 and turnoTirador == True:
        position_site[0] = position_site[0] + 60
        
    if (pygame.key.get_pressed()[pygame.K_p] == True) and position_site[0] != 840 and turnoTirador == False:
        position_site[0] = position_site[0] + 60

def lecturaFichas():
    turnoSiguiente = False
    if(pygame.key.get_pressed()[pygame.K_s] and turnoTirador == True):  # ficha roja
        c = position_site[0]
        j = position_site[1]
        copia_posicion = [c, j]
        listaRoja.insert(len(listaRoja)+1, copia_posicion)
        turnoSiguiente = False
    else:
        if(pygame.key.get_pressed()[pygame.K_o] and turnoTirador == False):  # ficha amarillas
            c = position_site[0]
            j = position_site[1]
            copia_posicion = [c, j]
            listaAmarilla.insert(len(listaAmarilla)+1, copia_posicion)
            turnoSiguiente = True
        else:
                turnoSiguiente = turnoTirador
           
    return turnoSiguiente

def fichaDesciende():
    for i in range(0, len(listaRoja), 1):
        if listaRoja[i][1] < (60*14) and pygame.Surface.get_at(SCREEN, (listaRoja[i][0],listaRoja[i][1]+60)) == green:
            listaRoja[i][1] = listaRoja[i][1] + 60
            
        
           
            
    for i in range(0, len(listaAmarilla), 1):
        if listaAmarilla[i][1] < (60*14) and pygame.Surface.get_at(SCREEN, (listaAmarilla[i][0],listaAmarilla[i][1]+60)) == green:
            listaAmarilla[i][1] = listaAmarilla[i][1] + 60
        
        
           
       
    pygame.display.update()   

def comprobacionGanadorRojo(ultimaFichaTirada):
    numeroFichasX = 0
    numeroFichasY = 0
    numeroFichasDP = 0
    numeroFichasDI = 0
    fichaComprobacionXX = ultimaFichaTirada[0]
    fichaComprobacionXY = ultimaFichaTirada[1]
    fichaComprobacionYX = ultimaFichaTirada[0]
    fichaComprobacionYY = ultimaFichaTirada[1]
    fichaComprobacionDPX = ultimaFichaTirada[0]
    fichaComprobacionDPY = ultimaFichaTirada[1]
    fichaComprobacionDIX = ultimaFichaTirada[0]
    fichaComprobacionDIY = ultimaFichaTirada[1]
    
    
    while pygame.Surface.get_at(SCREEN, (fichaComprobacionXX, fichaComprobacionXY)) == RED:
        numeroFichasX = numeroFichasX + 1
        fichaComprobacionXX = fichaComprobacionXX + 60
        if fichaComprobacionXX >= 870:
            break

    
    while pygame.Surface.get_at(SCREEN, (fichaComprobacionYX, fichaComprobacionYY)) == RED:
        numeroFichasY = numeroFichasY + 1
        fichaComprobacionYY = fichaComprobacionYY - 60
        if fichaComprobacionYY <= 0:
            break
        
    while pygame.Surface.get_at(SCREEN, (fichaComprobacionDPX, fichaComprobacionDPY)) == RED:
        numeroFichasDP = numeroFichasDP + 1
        fichaComprobacionDPX = fichaComprobacionDPX - 60
        fichaComprobacionDPY = fichaComprobacionDPY + 60
        if fichaComprobacionDPY >= 870 or fichaComprobacionDPX <= 0:
            break
        
    while pygame.Surface.get_at(SCREEN, (fichaComprobacionDIX, fichaComprobacionDIY)) == RED:
        numeroFichasDI = numeroFichasDI + 1
        fichaComprobacionDIX = fichaComprobacionDIX + 60
        fichaComprobacionDIY = fichaComprobacionDIY + 60
        if fichaComprobacionDIY >= 870 or fichaComprobacionDIX >= 870:
            break
    
    if numeroFichasX >= 4 or numeroFichasY >= 4 or numeroFichasDP >= 4 or numeroFichasDI >= 4:
        ganadoFinal(0)
        
        
        
        
def comprobacionGanadorAmarillo(ultimaFichaTirada):
    numeroFichasX = 0
    numeroFichasY = 0
    numeroFichasDP = 0
    numeroFichasDI = 0
    fichaComprobacionXX = ultimaFichaTirada[0]
    fichaComprobacionXY = ultimaFichaTirada[1]
    fichaComprobacionYX = ultimaFichaTirada[0]
    fichaComprobacionYY = ultimaFichaTirada[1]
    fichaComprobacionDPX = ultimaFichaTirada[0]
    fichaComprobacionDPY = ultimaFichaTirada[1]
    fichaComprobacionDIX = ultimaFichaTirada[0]
    fichaComprobacionDIY = ultimaFichaTirada[1]
    
    
    while pygame.Surface.get_at(SCREEN, (fichaComprobacionXX, fichaComprobacionXY)) == YELLOW:
        numeroFichasX = numeroFichasX + 1
        fichaComprobacionXX = fichaComprobacionXX + 60
        if fichaComprobacionXX >= 870:
            break

    
    while pygame.Surface.get_at(SCREEN, (fichaComprobacionYX, fichaComprobacionYY)) == YELLOW:
        numeroFichasY = numeroFichasY + 1
        fichaComprobacionYY = fichaComprobacionYY - 60
        if fichaComprobacionYY <= 0:
            break
        
    while pygame.Surface.get_at(SCREEN, (fichaComprobacionDPX, fichaComprobacionDPY)) == YELLOW:
        numeroFichasDP = numeroFichasDP + 1
        fichaComprobacionDPX = fichaComprobacionDPX - 60
        fichaComprobacionDPY = fichaComprobacionDPY + 60
        if fichaComprobacionDPY >= 870 or fichaComprobacionDPX <= 0:
            break
        
    while pygame.Surface.get_at(SCREEN, (fichaComprobacionDIX, fichaComprobacionDIY)) == YELLOW:
        numeroFichasDI = numeroFichasDI + 1
        fichaComprobacionDIX = fichaComprobacionDIX + 60
        fichaComprobacionDIY = fichaComprobacionDIY + 60
        if fichaComprobacionDIY >= 870 or fichaComprobacionDIX >= 870:
            break
    
    if numeroFichasX >= 4 or numeroFichasY >= 4 or numeroFichasDP >= 4 or numeroFichasDI >= 4:
        ganadoFinal(1)

def ganadoFinal(colorGanador):
  
    pygame.display.update()
    fuente = pygame.font.Font(None, 85)
    if colorGanador == 0:
        mensaje = fuente.render("Jugador Rojo GANADOR", 1, RED)
        SCREEN.blit(mensaje, (70, 400))
        pygame.display.update()
        pygame.time.delay(5000)
    else:
        if colorGanador == 1:
            mensaje = fuente.render("Jugador Amarillo GANADOR", 1, YELLOW)
            SCREEN.blit(mensaje, (45, 400))
            pygame.display.update()
            pygame.time.delay(5000)
            
  
        
    
    exit()
            
        


main()




