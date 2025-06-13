pygame
import sys

Ancho = 300
Altura = 300

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
AZUL = (0, 0, 255)
VERDE = (0, 255, 0)
MORADO = (128, 0, 128)
NARANJA = (255, 165, 0)

class Enemigo:
    def __init__(self, x, y, Ancho, Alto, color, eje='x'):
        self.x = x
        self.y = y
        self.Ancho = Ancho
        self.Alto = Alto
        self.color = color
        self.velocidad = 3
        self.eje = eje  import

    def mover_automatico(self): 
        if self.eje == 'x':
            self.x += self.velocidad
            if self.x < 0 or self.x + self.Ancho > Ancho:
                self.velocidad *= -1 
        elif self.eje == 'y   ':
            self.y += self.velocidad
            if self.y < 0 or self.y + self.Alto > Altura:
                self.velocidad *= -1

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, (self.x, self.y, self.Ancho, self.Alto))

# Inicializa pygame
pygame.init()
size = (300, 300)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Varios Enemigos")

clock = pygame.time.Clock()

# Lista de enemigos con diferentes atributos
enemigos = [
    Enemigo(0, 0, 40, 40, ROJO, 'x'),                       
    Enemigo(Ancho - 40, 0, 40, 40, AZUL, 'y'),                
    Enemigo(0, Altura - 40, 40, 40, VERDE, 'y'),                 
    Enemigo(Ancho - 40, Altura - 40, 40, 40, MORADO, 'x')     
]


# Bucle principal
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Lógica de movimiento
    for enemigo in enemigos:
        enemigo.mover_automatico()

    # Dibujar pantalla
    screen.fill(BLANCO)
    for enemigo in enemigos:
        enemigo.dibujar(screen)
    pygame.display.flip()

    clock.tick(60)

