import pygame
import os
import sys

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstaculos, jugador):
        super().__init__(groups)

        self.animacion_derecha = self.cargar_animacion("imagenes/enemigo/caminar_derecha")
        self.animacion_izquierda = self.cargar_animacion("imagenes/enemigo/caminar_izquierda")

        self.index_animacion = 0
        self.direccion = 1  # 1 para derecha, -1 para izquierda

        self.image = self.animacion_derecha[0]
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-50, -50)

        self.velocidad = 2
        self.obstaculos = obstaculos
        self.jugador = jugador

    def cargar_animacion(self, carpeta):
     imagenes = []
     for archivo in sorted(os.listdir(carpeta)):
        if archivo.endswith(".png"):
            ruta = os.path.join(carpeta, archivo)
            imagen = pygame.image.load(ruta).convert_alpha()
            imagenes.append(imagen)
     return imagenes


    def actualizar_animacion(self):
        self.index_animacion += 0.1 #para q avance fotograma por fotograma#
        if self.index_animacion >= len(self.animacion_derecha): #bucle de la imagenes
            self.index_animacion = 0

        if self.direccion == 1:
            self.image = self.animacion_derecha[int(self.index_animacion)] #elije la direccion
        else:
            self.image = self.animacion_izquierda[int(self.index_animacion)]#elije la direccion

    def colisiona_obstaculo(self):
        for obstaculo in self.obstaculos:
            if obstaculo.rect.colliderect(self.hitbox):
                return True
        return False

    def colisiona_jugador(self):
        return self.jugador.rect.colliderect(self.hitbox)

    def update(self):
        # Movimiento y rebote
        self.hitbox.x += self.velocidad * self.direccion
        if self.colisiona_obstaculo():
            self.hitbox.x -= self.velocidad * self.direccion
            self.direccion *= -1

        # Actualizar rect para dibujar
        self.rect.center = self.hitbox.center

        # Animación
        self.actualizar_animacion()

        # Colisión con jugador
        if self.colisiona_jugador():
            pygame.time.delay(500)
            print("¡Has perdido!")
            sys.exit()




