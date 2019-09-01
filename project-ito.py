# -*- coding: utf-8 -*-

# Módulos
import sys, pygame
import speech
from pygame.locals import *

# Constantes
WIDTH = 500
HEIGHT = 400

# Clases
# ---------------------------------------------------------------------

class Toad(pygame.sprite.Sprite):
    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("toad.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = HEIGHT / 2
        self.speed = 1

    def mover(self, time, keys):
        if self.rect.top >= 0:
            if keys[K_UP]:
                self.rect.centery -= self.speed * time
        if self.rect.bottom <= HEIGHT:
            if keys[K_DOWN]:
                self.rect.centery += self.speed * time 
        if self.rect.right >= 0:
            if keys[K_RIGHT]:
                self.rect.centerx += self.speed * time
        if self.rect.left <= WIDTH:
            if keys[K_LEFT]:
                self.rect.centerx -= self.speed * time
# ---------------------------------------------------------------------

# Funciones
# ---------------------------------------------------------------------

def load_image(filename, transparent=False):
        try: image = pygame.image.load(filename)
        except pygame.error, message : 
            raise SystemExit, message
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

"""def response(phrase, listener):
    global time, toad_jug
    speech.say("You said %s" % phrase)
    if phrase == "Arriba":
        carro_jug.rect.centery -= carro_jug.speed * time
    if phrase == "Abajo":
        carro_jug.rect.centery += carro_jug.speed * time 
    if phrase == "Acelerar Izquierda":
        carro_jug.rect.centerx -= carro_jug.speed * time
    if phrase == "Acelerar Derecha":
        carro_jug.rect.centerx += carro_jug.speed * time
    if phrase == "Salir":
        sys.exit() """

# ---------------------------------------------------------------------
toad_jug = None
time = None
def main():
    global time, toad_jug
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jueguito")

    background_image = load_image('laberinto.jpg')
    carro_jug = Toad(30)
    clock = pygame.time.Clock()

    listener = speech.listenfor(['Acelerar Derecha', 'Acelerar Izquierda', 'Arriba', 'Abajo', 'Salir'], response)
    while listener.islistening():
        time = clock.tick(60)
        keys = pygame.key.get_pressed()
        for eventos in pygame.event.get():
            if eventos.type == QUIT:
                sys.exit(0)

        toad_jug.mover(time, keys)
        screen.blit(background_image, (0, 0))
        screen.blit(toad_jug.image, toad_jug.rect)
        pygame.display.flip()
    return 0

if __name__ == '__main__':
    pygame.init()
    main()