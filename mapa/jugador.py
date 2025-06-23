import pygame
import os

class Jugador(pygame.sprite.Sprite):
    def __init__(self, pos, groups, obstaculos):
        super().__init__(groups)

        
        self.image = pygame.image.load("imagenes/image9x3.png")
        self.rect = self.image.get_rect(topleft=pos)
        self.hitbox = self.rect.inflate(-40, -40)

        self.direccion = pygame.math.Vector2()
        self.velocidad = 5
        self.Obstaculos = obstaculos

        
        self.frames_arriba = self.cargar_animaciones("personaje/caminar_arriba")
        self.frames_abajo = self.cargar_animaciones("personaje/caminar_abajo")
        self.frames_izquierda = self.cargar_animaciones("personaje/caminar_izquierda")
        self.frames_derecha = self.cargar_animaciones("personaje/caminar_derecha")

        self.frame_index = 0
        self.animacion_velocidad = 0.15
        self.direccion_actual = "abajo"

    def cargar_animaciones(self, carpeta):
        imagenes = []
        for nombre in sorted(os.listdir(carpeta)):#con el os.listdir accedemos a la carpeta y a sus elementos
            if nombre.endswith(".png"):
                ruta = os.path.join(carpeta, nombre)#con el os.patch accedemos a la ruta para tener una mejor exactitud de que archivo elejir
                imagenes.append(pygame.image.load(ruta).convert_alpha())
        return imagenes

    def teclado(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.direccion.y = -1
            self.direccion_actual = "arriba"
        elif keys[pygame.K_DOWN]:
            self.direccion.y = 1
            self.direccion_actual = "abajo"
        else:
            self.direccion.y = 0

        if keys[pygame.K_RIGHT]:
            self.direccion.x = 1
            self.direccion_actual = "derecha"
        elif keys[pygame.K_LEFT]:
            self.direccion.x = -1
            self.direccion_actual = "izquierda"
        else:
            self.direccion.x = 0

    def mover(self, velocidad):
        if self.direccion.magnitude() != 0:
            self.direccion = self.direccion.normalize()

        self.hitbox.x += self.direccion.x * velocidad
        self.colisiones("horizontal")
        self.hitbox.y += self.direccion.y * velocidad
        self.colisiones("vertical")
        self.rect.center = self.hitbox.center

    def colisiones(self, direccion):
        for sprite in self.Obstaculos:
            if sprite.rect.colliderect(self.hitbox):
                if direccion == "horizontal":
                    if self.direccion.x > 0:
                        self.hitbox.right = sprite.rect.left
                    elif self.direccion.x < 0:
                        self.hitbox.left = sprite.rect.right
                elif direccion == "vertical":
                    if self.direccion.y > 0:
                        self.hitbox.bottom = sprite.rect.top
                    elif self.direccion.y < 0:
                        self.hitbox.top = sprite.rect.bottom

    def animar(self):
        # Avanza el frame solo si el jugador se mueve
        if self.direccion.magnitude() != 0:
            self.frame_index += self.animacion_velocidad
            if self.frame_index >= len(self.frames_arriba):  # todas tienen el mismo largo
                self.frame_index = 0

            frame = int(self.frame_index)
            if self.direccion_actual == "arriba":
                self.image = self.frames_arriba[frame]
            elif self.direccion_actual == "abajo":
                self.image = self.frames_abajo[frame]
            elif self.direccion_actual == "izquierda":
                self.image = self.frames_izquierda[frame]
            elif self.direccion_actual == "derecha":
                self.image = self.frames_derecha[frame]
        else:
            self.frame_index = 0  # volver al primer frame cuando se detiene

    def update(self):
        self.teclado()
        self.mover(self.velocidad)
        self.animar()