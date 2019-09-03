import pygame
  
LEFT = 1
  
running = 1
screen = pygame.display.set_mode((320, 200))
  
while running:
   event = pygame.event.poll()
   if event.type == pygame.QUIT:
       running = 0
   elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
       print ("Se detecto un click izquierdo del raton en (%d, %d)" % event.pos)
   elif event.type == pygame.MOUSEBUTTONUP and event.button == LEFT:
       print ("Se solto el boton izquierdo del raton en(%d, %d)" % event.pos)

   screen.fill((0, 0, 0))
   pygame.display.flip()