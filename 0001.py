#!/usr/bin/python3
'''
Start date: 15.Jun.2k14
Author: HakitoCZ
Origin: bMt47wvK6u0
Indent set to 2 spaces. I may be wrong but I feel it clearer that way.
'''

import pygame


class Game(object):
  def main(self, screen):
    clock = pygame.time.Clock()

    image = pygame.image.load('player.png')
    image_x = 320
    image_y = 200

    while 1:
      clock.tick(30)

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          return
        if event.type == pygame.KEYDOWN and \
            event.key == pygame.K_ESCAPE:
          return

      key = pygame.key.get_pressed()
      if key[pygame.K_LEFT]:
        image_x -= 5
      if key[pygame.K_RIGHT]:
        image_x += 5
      if key[pygame.K_UP]:
        image_y -= 5
      if key[pygame.K_DOWN]:
        image_y += 5

      screen.fill((200, 200, 200))
      screen.blit(image, (image_x, image_y))
      pygame.display.flip()

if __name__ == '__main__':
  pygame.init()
  screen = pygame.display.set_mode((640, 400))
  Game().main(screen)

