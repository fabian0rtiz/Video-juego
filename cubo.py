import pygame
from variables import Ancho, Altura

class Jugador:
    def __init__(self, x, y, ancho, alto, color):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.color = color

    def manejar_eventos(self, event, paredes):
        dx, dy = 0, 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                dx = -20
                
            elif event.key == pygame.K_d:
                dx = 20
                
            elif event.key == pygame.K_w:
                dy = -20
               
            elif event.key == pygame.K_s:
                dy = 20
               
            self.mover(dx, dy, paredes)#esto detendra al cubo para que no se vaya al infinito

    def mover(self, dx, dy, paredes):
        nuevo_rect = pygame.Rect(self.x + dx, self.y + dy, self.ancho, self.alto)
        colisiona = any(nuevo_rect.colliderect(p) 
                        for p in paredes) #esto tengo que modificarlo ya que aun no hay mapa de matriz 

        if not colisiona:
            self.x += dx
            self.y += dy

        
        if self.x < 0 or self.x > Ancho - self.ancho:
            self.x -= dx  #Esto cambia la direccion para que no salgaaa de pantalla en horizontal
           

        if self.y < 0 or self.y > Altura - self.alto:
            self.y -= dy#esto cambia la direccion para que no salga de la pantalla en vertical
            

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.ancho, self.alto))
