# -*- coding: utf-8 -*-

# Módulos
import sys
import pygame
import speech_recognition as sr
from pygame.locals import *

# Constantess
WIDTH = 1000
HEIGHT = 500


# Clases
# ---------------------------------------------------------------------

class Toad(pygame.sprite.Sprite):

    def __init__(self, x):
        pygame.sprite.Sprite.__init__(self)
        self.image = load_image("toad.jpg")
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = HEIGHT / 8
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
        try: image = pygame.image.load("laberinto.jpg")
        except pygame.error as message: 
            raise 
            SystemExit(message)
        image = image.convert()
        if transparent:
                color = image.get_at((0,0))
                image.set_colorkey(color, RLEACCEL)
        return image

def response(phrase, listener):
    global time, toad_jug
    sr.say("Moved to %s" % phrase) 
    if phrase == "Arriba":
        toad_jug.rect.centery -= toad_jug.speed * time
    if phrase == "Abajo":
        toad_jug.rect.centery += toad_jug.speed * time 
    if phrase == "Izquierda":
        toad_jug.rect.centerx -= toad_jug.speed * time
    if phrase == "Derecha":
        toad_jug.rect.centerx += toad_jug.speed * time
    if phrase == "Salir":
        sys.exit() 

# ---------------------------------------------------------------------
toad_jug = None
time = None
def main():
    global time, toad_jug
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Jueguito")

    background_image = load_image('laberinto.jpg')
    toad_jug = Toad(30)
    clock = pygame.time.Clock()

    listener = sr.listenfor(['Derecha', 'Izquierda', 'Arriba', 'Abajo', 'Salir'], response)
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
