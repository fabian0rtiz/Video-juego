import pygame
import os

class Enemigo(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstaculos, jugador):
        super().__init__(groups)
        self.obstaculos = obstaculos
        self.jugador = jugador

        self.animacion_derecha = self.cargar_animacion("enemigo/caminar_derecha")
        self.animacion_izquierda = self.cargar_animacion("enemigo/caminar_izquierda")
        self.direccion = 1  # 1 para derecha, -1 para izquierda
        self.index_anim = 0
        self.image = self.animacion_derecha[0]
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(0, -20)
        self.velocidad = 2

    def cargar_animacion(self, carpeta):
        imagenes = []
        for archivo in sorted(os.listdir(carpeta)):
            if archivo.endswith(".png"):
                ruta = os.path.join(carpeta, archivo)
                imagen = pygame.image.load(ruta).convert_alpha()
                imagenes.append(imagen)
        return imagenes

    def mover(self):
        self.hitbox.x += self.velocidad * self.direccion
        self.colisiones()
        self.rect.center = self.hitbox.center

    def colisiones(self):
        for sprite in self.obstaculos:
            if sprite.rect.colliderect(self.hitbox):
                self.direccion *= -1  # Rebotar
                return

    def animar(self):
        self.index_anim += 0.1
        if self.index_anim >= len(self.animacion_derecha):
            self.index_anim = 0
        if self.direccion > 0:
            self.image = self.animacion_derecha[int(self.index_anim)]
        else:
            self.image = self.animacion_izquierda[int(self.index_anim)]

    def update(self):
        self.mover()
        self.animar()

        # Colisión con jugador
        if self.jugador.rect.colliderect(self.rect):
            self.jugador.morir()  # Deberás implementar esto en el jugador
